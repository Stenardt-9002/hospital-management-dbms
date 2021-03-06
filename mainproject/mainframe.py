#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Thu Apr 11 02:02:01 2019
#

import wx
import Dep2 as Dew

import wx.grid

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1382, 744))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.notebook_1 = wx.Notebook(self.panel_1, wx.ID_ANY)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY, style=wx.BORDER_STATIC | wx.TAB_TRAVERSAL)
        self.notebook_1_Departments = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_2 = wx.Panel(self.notebook_1_Departments, wx.ID_ANY)
        self.button_1 = wx.Button(self.notebook_1_Departments, wx.ID_ANY, "+ADD Dept")
        self.button_2 = wx.Button(self.notebook_1_Departments, wx.ID_ANY, "Delete ")
        self.panel_3 = wx.Panel(self.notebook_1_Departments, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.notebook_1_Departments, wx.ID_ANY, "Enter Dept No..")
        self.button_3 = wx.Button(self.notebook_1_Departments, wx.ID_ANY, "Search")
        self.grid_1 = wx.grid.Grid(self.notebook_1_Departments, wx.ID_ANY, size=(1, 1))
        self.notebook_1_Patients = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_4 = wx.Panel(self.notebook_1_Patients, wx.ID_ANY)
        self.button_4 = wx.Button(self.notebook_1_Patients, wx.ID_ANY, "+ADD Patient")
        self.button_5 = wx.Button(self.notebook_1_Patients, wx.ID_ANY, "Delete ")
        self.panel_5 = wx.Panel(self.notebook_1_Patients, wx.ID_ANY)
        self.text_ctrl_2 = wx.TextCtrl(self.notebook_1_Patients, wx.ID_ANY, "Enter Patient No..", style=wx.TE_LEFT)
        self.button_6 = wx.Button(self.notebook_1_Patients, wx.ID_ANY, "Search")
        self.grid_2 = wx.grid.Grid(self.notebook_1_Patients, wx.ID_ANY, size=(1, 1))
        self.notebook_1_Doctors = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_6 = wx.Panel(self.notebook_1_Doctors, wx.ID_ANY)
        self.button_7 = wx.Button(self.notebook_1_Doctors, wx.ID_ANY, "+ADD Dept")
        self.button_8 = wx.Button(self.notebook_1_Doctors, wx.ID_ANY, "Delete ")
        self.panel_7 = wx.Panel(self.notebook_1_Doctors, wx.ID_ANY)
        self.text_ctrl_3 = wx.TextCtrl(self.notebook_1_Doctors, wx.ID_ANY, "")
        self.button_9 = wx.Button(self.notebook_1_Doctors, wx.ID_ANY, "Search")
        self.grid_3 = wx.grid.Grid(self.notebook_1_Doctors, wx.ID_ANY, size=(1, 1))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.Depart, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Hospital Management System")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Inspiron\\Desktop\\1.jpg", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.notebook_1_pane_2.SetFont(wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Bernard MT Condensed"))
        self.panel_2.SetMinSize((1209, 50))
        self.button_1.SetMinSize((130, 50))
        self.button_1.SetBackgroundColour(wx.Colour(0, 165, 0))
        self.button_1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_1.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.button_2.SetMinSize((130, 50))
        self.button_2.SetBackgroundColour(wx.Colour(204, 50, 50))
        self.button_2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_2.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.panel_3.SetMinSize((600, 50))
        self.text_ctrl_1.SetMinSize((150, 30))
        self.button_3.SetMinSize((130, 50))
        self.button_3.SetBackgroundColour(wx.Colour(0, 165, 0))
        self.button_3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_3.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.grid_1.CreateGrid(10, 3)
        self.grid_1.EnableEditing(0)
        self.grid_1.SetColLabelValue(0, "DEPT_NO")
        self.grid_1.SetColLabelValue(1, "DEPT_Name")
        self.grid_1.SetColSize(1, 148)
        self.grid_1.SetColLabelValue(2, "Description")
        self.grid_1.SetColSize(2, 577)
        self.panel_4.SetMinSize((1209, 50))
        self.button_4.SetMinSize((150, 50))
        self.button_4.SetBackgroundColour(wx.Colour(0, 165, 0))
        self.button_4.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_4.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.button_5.SetMinSize((130, 50))
        self.button_5.SetBackgroundColour(wx.Colour(204, 50, 50))
        self.button_5.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_5.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.panel_5.SetMinSize((600, 50))
        self.text_ctrl_2.SetMinSize((150, 30))
        self.button_6.SetMinSize((130, 50))
        self.button_6.SetBackgroundColour(wx.Colour(0, 165, 0))
        self.button_6.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_6.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.grid_2.CreateGrid(10, 3)
        self.grid_2.EnableEditing(0)
        self.grid_2.SetColLabelValue(0, "DEPT_NO")
        self.grid_2.SetColLabelValue(1, "DEPT_Name")
        self.grid_2.SetColSize(1, 148)
        self.grid_2.SetColLabelValue(2, "Description")
        self.grid_2.SetColSize(2, 577)
        self.notebook_1_Patients.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        self.panel_6.SetMinSize((1209, 50))
        self.button_7.SetMinSize((130, 50))
        self.button_7.SetBackgroundColour(wx.Colour(0, 165, 0))
        self.button_7.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_7.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.button_8.SetMinSize((130, 50))
        self.button_8.SetBackgroundColour(wx.Colour(204, 50, 50))
        self.button_8.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_8.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.panel_7.SetMinSize((600, 50))
        self.text_ctrl_3.SetMinSize((150, 30))
        self.button_9.SetMinSize((130, 50))
        self.button_9.SetBackgroundColour(wx.Colour(0, 165, 0))
        self.button_9.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button_9.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Rockwell"))
        self.grid_3.CreateGrid(10, 3)
        self.grid_3.EnableEditing(0)
        self.grid_3.SetColLabelValue(0, "DEPT_NO")
        self.grid_3.SetColLabelValue(1, "DEPT_Name")
        self.grid_3.SetColSize(1, 148)
        self.grid_3.SetColLabelValue(2, "Description")
        self.grid_3.SetColSize(2, 577)
        self.notebook_1.SetFont(wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Palatino Linotype"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.BoxSizer(wx.VERTICAL)
        sizer_27 = wx.BoxSizer(wx.VERTICAL)
        sizer_30 = wx.BoxSizer(wx.VERTICAL)
        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_28 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.VERTICAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_19 = wx.BoxSizer(wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.VERTICAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        bitmap_1 = wx.StaticBitmap(self.notebook_1_pane_2, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\symbion-hospital-services-vector-logo-small.jpg", wx.BITMAP_TYPE_ANY))
        bitmap_1.SetMinSize((300, 100))
        sizer_6.Add(bitmap_1, 0, 0, 0)
        label_1 = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, "Welcome to Symbion Hospital Services", style=wx.ALIGN_CENTER)
        label_1.SetBackgroundColour(wx.Colour(216, 191, 216))
        label_1.SetForegroundColour(wx.Colour(35, 35, 142))
        label_1.SetFont(wx.Font(35, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Trebuchet MS"))
        sizer_6.Add(label_1, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 7)
        sizer_3.Add(sizer_6, 0, wx.ALL | wx.EXPAND, 11)
        static_line_1 = wx.StaticLine(self.notebook_1_pane_2, wx.ID_ANY)
        sizer_4.Add(static_line_1, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, "\nDashboard ", style=wx.ALIGN_CENTER | wx.ALIGN_LEFT)
        label_2.SetMinSize((200, 70))
        label_2.SetBackgroundColour(wx.Colour(192, 192, 192))
        label_2.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Cooper Black"))
        sizer_5.Add(label_2, 0, wx.ALIGN_CENTER, 0)
        label_3 = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, "\nHome", style=wx.ALIGN_CENTER)
        label_3.SetFont(wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Centaur"))
        sizer_5.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        static_line_2 = wx.StaticLine(self.notebook_1_pane_2, wx.ID_ANY)
        sizer_4.Add(static_line_2, 0, wx.EXPAND, 0)
        bitmap_2 = wx.StaticBitmap(self.notebook_1_pane_2, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\13986.jpg", wx.BITMAP_TYPE_ANY))
        sizer_4.Add(bitmap_2, 0, 0, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_3)
        bitmap_3 = wx.StaticBitmap(self.notebook_1_Departments, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\Our-Departments.jpg", wx.BITMAP_TYPE_ANY))
        sizer_7.Add(bitmap_3, 0, 0, 0)
        bitmap_4 = wx.StaticBitmap(self.notebook_1_Departments, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\symbion-hospital-services-vector-logo-small.jpg", wx.BITMAP_TYPE_ANY))
        bitmap_4.SetMinSize((300, 100))
        sizer_10.Add(bitmap_4, 0, 0, 0)
        label_4 = wx.StaticText(self.notebook_1_Departments, wx.ID_ANY, "  Welcome to Symbion Hospital Services              ", style=wx.ALIGN_CENTER)
        label_4.SetBackgroundColour(wx.Colour(216, 191, 216))
        label_4.SetForegroundColour(wx.Colour(35, 35, 142))
        label_4.SetFont(wx.Font(35, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Trebuchet MS"))
        sizer_10.Add(label_4, 1, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.TOP, 7)
        sizer_9.Add(sizer_10, 0, wx.ALL | wx.EXPAND, 5)
        sizer_8.Add(sizer_9, 0, 0, 0)
        static_line_3 = wx.StaticLine(self.notebook_1_Departments, wx.ID_ANY)
        sizer_11.Add(static_line_3, 0, wx.EXPAND, 0)
        bitmap_5 = wx.StaticBitmap(self.notebook_1_Departments, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\d1 (1).jpg", wx.BITMAP_TYPE_ANY))
        bitmap_5.SetMinSize((50, 50))
        sizer_12.Add(bitmap_5, 0, 0, 0)
        label_5 = wx.StaticText(self.notebook_1_Departments, wx.ID_ANY, "Department List")
        label_5.SetBackgroundColour(wx.Colour(219, 200, 208))
        label_5.SetFont(wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Verdana"))
        sizer_12.Add(label_5, 1, wx.EXPAND, 0)
        sizer_11.Add(sizer_12, 0, wx.EXPAND, 0)
        static_line_4 = wx.StaticLine(self.notebook_1_Departments, wx.ID_ANY)
        sizer_11.Add(static_line_4, 0, wx.EXPAND, 0)
        sizer_11.Add(self.panel_2, 0, wx.EXPAND, 0)
        sizer_13.Add(self.button_1, 0, wx.EXPAND, 0)
        sizer_13.Add(self.button_2, 0, wx.EXPAND, 0)
        sizer_13.Add(self.panel_3, 0, wx.EXPAND, 0)
        sizer_13.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER, 0)
        sizer_13.Add(self.button_3, 0, wx.ALIGN_RIGHT | wx.EXPAND, 0)
        sizer_11.Add(sizer_13, 0, wx.EXPAND, 0)
        sizer_14.Add((0, 7), 0, 0, 0)
        sizer_14.Add(self.grid_1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_11.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_8.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
        self.notebook_1_Departments.SetSizer(sizer_7)
        bitmap_6 = wx.StaticBitmap(self.notebook_1_Patients, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\Our-Departments1-001.jpg", wx.BITMAP_TYPE_ANY))
        sizer_15.Add(bitmap_6, 0, 0, 0)
        bitmap_7 = wx.StaticBitmap(self.notebook_1_Patients, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\symbion-hospital-services-vector-logo-small.jpg", wx.BITMAP_TYPE_ANY))
        bitmap_7.SetMinSize((300, 100))
        sizer_18.Add(bitmap_7, 0, 0, 0)
        label_6 = wx.StaticText(self.notebook_1_Patients, wx.ID_ANY, "  Welcome to Symbion Hospital Services              ", style=wx.ALIGN_CENTER)
        label_6.SetBackgroundColour(wx.Colour(216, 191, 216))
        label_6.SetForegroundColour(wx.Colour(35, 35, 142))
        label_6.SetFont(wx.Font(35, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Trebuchet MS"))
        sizer_18.Add(label_6, 1, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.TOP, 7)
        sizer_17.Add(sizer_18, 0, wx.ALL | wx.EXPAND, 5)
        sizer_16.Add(sizer_17, 0, 0, 0)
        static_line_5 = wx.StaticLine(self.notebook_1_Patients, wx.ID_ANY)
        sizer_19.Add(static_line_5, 0, wx.EXPAND, 0)
        bitmap_8 = wx.StaticBitmap(self.notebook_1_Patients, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\d1 (1).jpg", wx.BITMAP_TYPE_ANY))
        bitmap_8.SetMinSize((50, 50))
        sizer_20.Add(bitmap_8, 0, 0, 0)
        label_7 = wx.StaticText(self.notebook_1_Patients, wx.ID_ANY, "Patient List")
        label_7.SetBackgroundColour(wx.Colour(219, 200, 208))
        label_7.SetFont(wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Verdana"))
        sizer_20.Add(label_7, 1, wx.EXPAND, 0)
        sizer_19.Add(sizer_20, 0, wx.EXPAND, 0)
        static_line_6 = wx.StaticLine(self.notebook_1_Patients, wx.ID_ANY)
        sizer_19.Add(static_line_6, 0, wx.EXPAND, 0)
        sizer_19.Add(self.panel_4, 0, wx.EXPAND, 0)
        sizer_21.Add(self.button_4, 0, wx.EXPAND, 0)
        sizer_21.Add(self.button_5, 0, wx.EXPAND, 0)
        sizer_21.Add(self.panel_5, 0, wx.EXPAND, 0)
        sizer_21.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER, 0)
        sizer_21.Add(self.button_6, 0, wx.ALIGN_RIGHT | wx.EXPAND, 0)
        sizer_19.Add(sizer_21, 0, wx.EXPAND, 0)
        sizer_22.Add((0, 7), 0, 0, 0)
        sizer_22.Add(self.grid_2, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_19.Add(sizer_22, 1, wx.EXPAND, 0)
        sizer_16.Add(sizer_19, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_16, 1, wx.EXPAND, 0)
        self.notebook_1_Patients.SetSizer(sizer_15)
        bitmap_9 = wx.StaticBitmap(self.notebook_1_Doctors, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\Our-Departments.jpg", wx.BITMAP_TYPE_ANY))
        sizer_23.Add(bitmap_9, 0, 0, 0)
        bitmap_10 = wx.StaticBitmap(self.notebook_1_Doctors, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\symbion-hospital-services-vector-logo-small.jpg", wx.BITMAP_TYPE_ANY))
        bitmap_10.SetMinSize((300, 100))
        sizer_26.Add(bitmap_10, 0, 0, 0)
        label_8 = wx.StaticText(self.notebook_1_Doctors, wx.ID_ANY, "  Welcome to Symbion Hospital Services              ", style=wx.ALIGN_CENTER)
        label_8.SetBackgroundColour(wx.Colour(216, 191, 216))
        label_8.SetForegroundColour(wx.Colour(35, 35, 142))
        label_8.SetFont(wx.Font(35, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Trebuchet MS"))
        sizer_26.Add(label_8, 1, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.TOP, 7)
        sizer_25.Add(sizer_26, 0, wx.ALL | wx.EXPAND, 5)
        sizer_24.Add(sizer_25, 0, 0, 0)
        static_line_7 = wx.StaticLine(self.notebook_1_Doctors, wx.ID_ANY)
        sizer_27.Add(static_line_7, 0, wx.EXPAND, 0)
        bitmap_11 = wx.StaticBitmap(self.notebook_1_Doctors, wx.ID_ANY, wx.Bitmap("E:\\Python\\DBMS Project\\Hospital (wxglade)\\Images\\d1 (1).jpg", wx.BITMAP_TYPE_ANY))
        bitmap_11.SetMinSize((50, 50))
        sizer_28.Add(bitmap_11, 0, 0, 0)
        label_9 = wx.StaticText(self.notebook_1_Doctors, wx.ID_ANY, "Department List")
        label_9.SetBackgroundColour(wx.Colour(219, 200, 208))
        label_9.SetFont(wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Verdana"))
        sizer_28.Add(label_9, 1, wx.EXPAND, 0)
        sizer_27.Add(sizer_28, 0, wx.EXPAND, 0)
        static_line_8 = wx.StaticLine(self.notebook_1_Doctors, wx.ID_ANY)
        sizer_27.Add(static_line_8, 0, wx.EXPAND, 0)
        sizer_27.Add(self.panel_6, 0, wx.EXPAND, 0)
        sizer_29.Add(self.button_7, 0, wx.EXPAND, 0)
        sizer_29.Add(self.button_8, 0, wx.EXPAND, 0)
        sizer_29.Add(self.panel_7, 0, wx.EXPAND, 0)
        sizer_29.Add(self.text_ctrl_3, 0, wx.ALIGN_CENTER, 0)
        sizer_29.Add(self.button_9, 0, wx.ALIGN_RIGHT | wx.EXPAND, 0)
        sizer_27.Add(sizer_29, 0, wx.EXPAND, 0)
        sizer_30.Add((0, 7), 0, 0, 0)
        sizer_30.Add(self.grid_3, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_27.Add(sizer_30, 1, wx.EXPAND, 0)
        sizer_24.Add(sizer_27, 1, wx.EXPAND, 0)
        sizer_23.Add(sizer_24, 1, wx.EXPAND, 0)
        self.notebook_1_Doctors.SetSizer(sizer_23)
        self.notebook_1.AddPage(self.notebook_1_pane_2, "  Home  ")
        self.notebook_1.AddPage(self.notebook_1_Departments, "  Department  ")
        self.notebook_1.AddPage(self.notebook_1_Patients, "  Patients  ")
        self.notebook_1.AddPage(self.notebook_1_Doctors, "  Doctors  ")
        sizer_2.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def Depart(self, event):  # wxGlade: MyFrame.<event_handler>
        # print("Event handler 'Depart' not implemented!")
        Dew.initial()

        event.Skip()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
