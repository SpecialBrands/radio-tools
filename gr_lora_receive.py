#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Lora Receive
# Generated: Tue Jan 16 16:30:12 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import lora
import osmosdr
import time
import wx


class gr_lora_receive(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Gr Lora Receive")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3e6
        self.offset = offset = -26e3
        self.freq = freq = 868.1e6
        self.ch_freq = ch_freq = 868e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=30,
        	average=True,
        	avg_alpha=None,
        	title="LoRa 868 plot",
        	peak_hold=True,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        def wxgui_fftsink2_0_callback(x, y):
        	self.set_freq(x)
        
        self.wxgui_fftsink2_0.set_callback(wxgui_fftsink2_0_callback)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(ch_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.lora_message_socket_sink_0 = lora.message_socket_sink("127.0.0.1", 40868, 0)
        self.lora_lora_receiver_0 = lora.lora_receiver(1e6, 868e6, ([868.1e6]), 7, 1000000, False, 4, True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_lora_receiver_0, 'frames'), (self.lora_message_socket_sink_0, 'in'))    
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.lora_lora_receiver_0.set_center_freq(self.freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.freq)

    def get_ch_freq(self):
        return self.ch_freq

    def set_ch_freq(self, ch_freq):
        self.ch_freq = ch_freq
        self.osmosdr_source_0.set_center_freq(self.ch_freq, 0)


def main(top_block_cls=gr_lora_receive, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
