# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Layton Editor", pos = wx.DefaultPosition, size = wx.Size( 624,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 600,600 ), wx.DefaultSize )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel_leftside = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_leftside.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		bSizer_leftside = wx.BoxSizer( wx.VERTICAL )

		self.tree_imagefiles = wx.TreeCtrl( self.m_panel_leftside, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer_leftside.Add( self.tree_imagefiles, 1, wx.EXPAND|wx.ALL, 5 )

		gSizer_buttonsleft = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button_extract = wx.Button( self.m_panel_leftside, wx.ID_ANY, u"Extract", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_buttonsleft.Add( self.m_button_extract, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_replacefile = wx.Button( self.m_panel_leftside, wx.ID_ANY, u"Replace", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_buttonsleft.Add( self.m_button_replacefile, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_extractdecom = wx.Button( self.m_panel_leftside, wx.ID_ANY, u"Extract Decompressed", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_buttonsleft.Add( self.m_button_extractdecom, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button23 = wx.Button( self.m_panel_leftside, wx.ID_ANY, u"Replace Decompressed", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_buttonsleft.Add( self.m_button23, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer_leftside.Add( gSizer_buttonsleft, 0, wx.EXPAND, 5 )


		self.m_panel_leftside.SetSizer( bSizer_leftside )
		self.m_panel_leftside.Layout()
		bSizer_leftside.Fit( self.m_panel_leftside )
		bSizer14.Add( self.m_panel_leftside, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_imageinfo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_imageinfo.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		bSizer_imageinfo = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_previewimage = wx.Panel( self.m_panel_imageinfo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_previewimage.SetMinSize( wx.Size( 276,202 ) )

		bSizer_previewimage = wx.BoxSizer( wx.VERTICAL )

		self.previewImage = wx.StaticBitmap( self.m_panel_previewimage, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.previewImage.SetMinSize( wx.Size( 256,192 ) )

		bSizer_previewimage.Add( self.previewImage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel_previewimage.SetSizer( bSizer_previewimage )
		self.m_panel_previewimage.Layout()
		bSizer_previewimage.Fit( self.m_panel_previewimage )
		bSizer_imageinfo.Add( self.m_panel_previewimage, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer_selectimage = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_previousimage = wx.Button( self.m_panel_imageinfo, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer_selectimage.Add( self.m_button_previousimage, 1, wx.ALL, 5 )

		self.m_staticText_currentimage = wx.StaticText( self.m_panel_imageinfo, wx.ID_ANY, u"0/0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText_currentimage.Wrap( -1 )

		bSizer_selectimage.Add( self.m_staticText_currentimage, 1, wx.ALL, 10 )

		self.m_button_nextimage = wx.Button( self.m_panel_imageinfo, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer_selectimage.Add( self.m_button_nextimage, 1, wx.ALL, 5 )


		bSizer_imageinfo.Add( bSizer_selectimage, 0, wx.EXPAND, 5 )

		self.m_staticText_Colordepth = wx.StaticText( self.m_panel_imageinfo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText_Colordepth.Wrap( -1 )

		bSizer_imageinfo.Add( self.m_staticText_Colordepth, 0, wx.ALL, 5 )

		self.m_staticText_imagename = wx.StaticText( self.m_panel_imageinfo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText_imagename.Wrap( -1 )

		bSizer_imageinfo.Add( self.m_staticText_imagename, 0, wx.ALL, 5 )

		self.m_staticText_imageID = wx.StaticText( self.m_panel_imageinfo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText_imageID.Wrap( -1 )

		bSizer_imageinfo.Add( self.m_staticText_imageID, 0, wx.ALL, 5 )

		self.m_panel_filler = wx.Panel( self.m_panel_imageinfo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_imageinfo.Add( self.m_panel_filler, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button_saveimage = wx.Button( self.m_panel_imageinfo, wx.ID_ANY, u"Save Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_imageinfo.Add( self.m_button_saveimage, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_replaceimage = wx.Button( self.m_panel_imageinfo, wx.ID_ANY, u"Replace Image (no palette change)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_imageinfo.Add( self.m_button_replaceimage, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_replaceimageandpalette = wx.Button( self.m_panel_imageinfo, wx.ID_ANY, u"Replace Image (add to palette)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_imageinfo.Add( self.m_button_replaceimageandpalette, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_editimage = wx.Button( self.m_panel_imageinfo, wx.ID_ANY, u"Edit (dummy for future versions)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_imageinfo.Add( self.m_button_editimage, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_imageinfo.SetSizer( bSizer_imageinfo )
		self.m_panel_imageinfo.Layout()
		bSizer_imageinfo.Fit( self.m_panel_imageinfo )
		bSizer14.Add( self.m_panel_imageinfo, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer14, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizer13 )
		self.Layout()
		self.m_menubar_windowmenu = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_openfile = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_openfile )

		self.m_menuItem_savefile = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_savefile )

		self.m_menuItem_savefileas = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_savefileas )

		self.m_menubar_windowmenu.Append( self.m_menu_file, u"File" )

		self.SetMenuBar( self.m_menubar_windowmenu )


		self.Centre( wx.HORIZONTAL )

		# Connect Events
		self.tree_imagefiles.Bind( wx.EVT_TREE_SEL_CHANGED, self.tree_imagefilesOnTreeSelChanged )
		self.m_button_extract.Bind( wx.EVT_BUTTON, self.OnButtonClickExtract )
		self.m_button_replacefile.Bind( wx.EVT_BUTTON, self.OnButtonClickReplace )
		self.m_button_extractdecom.Bind( wx.EVT_BUTTON, self.OnButtonClickExtractDecom )
		self.m_button23.Bind( wx.EVT_BUTTON, self.OnButtonClickReplaceDecom )
		self.m_button_previousimage.Bind( wx.EVT_BUTTON, self.OnButtonClickPreviousImage )
		self.m_button_nextimage.Bind( wx.EVT_BUTTON, self.OnButtonClickNextImage )
		self.m_button_saveimage.Bind( wx.EVT_BUTTON, self.OnButtonClickSaveImage )
		self.m_button_replaceimage.Bind( wx.EVT_BUTTON, self.OnButtonClickReplaceImage )
		self.m_button_replaceimageandpalette.Bind( wx.EVT_BUTTON, self.OnButtonClickReplaceImageAddPall )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionOpen, id = self.m_menuItem_openfile.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSave, id = self.m_menuItem_savefile.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionSaveAs, id = self.m_menuItem_savefileas.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tree_imagefilesOnTreeSelChanged( self, event ):
		event.Skip()

	def OnButtonClickExtract( self, event ):
		event.Skip()

	def OnButtonClickReplace( self, event ):
		event.Skip()

	def OnButtonClickExtractDecom( self, event ):
		event.Skip()

	def OnButtonClickReplaceDecom( self, event ):
		event.Skip()

	def OnButtonClickPreviousImage( self, event ):
		event.Skip()

	def OnButtonClickNextImage( self, event ):
		event.Skip()

	def OnButtonClickSaveImage( self, event ):
		event.Skip()

	def OnButtonClickReplaceImage( self, event ):
		event.Skip()

	def OnButtonClickReplaceImageAddPall( self, event ):
		event.Skip()

	def OnMenuSelectionOpen( self, event ):
		event.Skip()

	def OnMenuSelectionSave( self, event ):
		event.Skip()

	def OnMenuSelectionSaveAs( self, event ):
		event.Skip()


###########################################################################
## Class ImageEdit
###########################################################################

class ImageEdit ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Image", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap3 = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap3.SetMinSize( wx.Size( 256,192 ) )

		bSizer21.Add( self.m_bitmap3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button8 = wx.Button( self.m_panel3, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer11.Add( self.m_button8, 1, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"1/1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText5.Wrap( -1 )

		bSizer11.Add( self.m_staticText5, 1, wx.ALL, 10 )

		self.m_button9 = wx.Button( self.m_panel3, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer11.Add( self.m_button9, 1, wx.ALL, 5 )


		bSizer21.Add( bSizer11, 0, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ID: 0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText9.Wrap( -1 )

		bSizer21.Add( self.m_staticText9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"i.jpg", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer21.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Colordepth: 4bit", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText7.Wrap( -1 )

		bSizer21.Add( self.m_staticText7, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button30 = wx.Button( self.m_panel3, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button30, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button31 = wx.Button( self.m_panel3, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button31, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button32 = wx.Button( self.m_panel3, wx.ID_ANY, u"Add Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button32, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button33 = wx.Button( self.m_panel3, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button33, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button43 = wx.Button( self.m_panel3, wx.ID_ANY, u"Import All", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button43, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button42 = wx.Button( self.m_panel3, wx.ID_ANY, u"Export All", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button42, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer21.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer21 )
		self.m_panel3.Layout()
		bSizer21.Fit( self.m_panel3 )
		bSizer19.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button81 = wx.Button( self.m_panel4, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer111.Add( self.m_button81, 1, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"1/1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText51.Wrap( -1 )

		bSizer111.Add( self.m_staticText51, 1, wx.ALL, 10 )

		self.m_button91 = wx.Button( self.m_panel4, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer111.Add( self.m_button91, 1, wx.ALL, 5 )


		bSizer15.Add( bSizer111, 0, wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"Create an Animation", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		self.m_textCtrl1.SetMaxLength( 24 )
		bSizer15.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		m_checkList1Choices = [u"Image 1"]
		self.m_checkList1 = wx.CheckListBox( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
		bSizer15.Add( self.m_checkList1, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button19 = wx.Button( self.m_panel4, wx.ID_ANY, u"Add Animation", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button19, 1, wx.ALL, 5 )

		self.m_button20 = wx.Button( self.m_panel4, wx.ID_ANY, u"Remove Animation", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button20, 1, wx.ALL, 5 )


		bSizer15.Add( bSizer14, 0, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer15 )
		self.m_panel4.Layout()
		bSizer15.Fit( self.m_panel4 )
		bSizer19.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer18.Add( bSizer19, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer18 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

