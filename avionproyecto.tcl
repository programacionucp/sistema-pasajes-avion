#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Apr 19, 2020 04:00:56 PM -03  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top43 {base} {
    global vTcl
    if {$base == ""} {
        set base .top43
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m55" -background #008040 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1117x500+137+128
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    set site_3_0 $top.m55
    menu $site_3_0 \
        -activebackground SystemHighlight \
        -activeforeground SystemHighlightText \
        -background $vTcl(pr,menubgcolor) -font TkDefaultFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    canvas $top.can84 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 468 -highlightbackground #e1c6ec -highlightcolor black \
        -insertbackground black -relief sunken -selectbackground #008040 \
        -selectforeground black -width 1065 
    vTcl:DefineAlias "$top.can84" "Canvas2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.can84
    label $site_3_0.lab86 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 1 
    vTcl:DefineAlias "$site_3_0.lab86" "asiento1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab89 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 2 
    vTcl:DefineAlias "$site_3_0.lab89" "asiento2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab90 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 3 
    vTcl:DefineAlias "$site_3_0.lab90" "asiento3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab91 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 4 
    vTcl:DefineAlias "$site_3_0.lab91" "asiento4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab92 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 7 
    vTcl:DefineAlias "$site_3_0.lab92" "asiento7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab93 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 5 
    vTcl:DefineAlias "$site_3_0.lab93" "asiento5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab94 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 6 
    vTcl:DefineAlias "$site_3_0.lab94" "asiento6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab96 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #efe136 -borderwidth 6 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 8 
    vTcl:DefineAlias "$site_3_0.lab96" "asiento8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab97 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 9 
    vTcl:DefineAlias "$site_3_0.lab97" "asiento9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab98 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 10 
    vTcl:DefineAlias "$site_3_0.lab98" "asiento10" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab99 \
        -activebackground #0000a0 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 11 
    vTcl:DefineAlias "$site_3_0.lab99" "asiento11" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab100 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 13 
    vTcl:DefineAlias "$site_3_0.lab100" "asiento13" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab102 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 14 
    vTcl:DefineAlias "$site_3_0.lab102" "asiento14" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab103 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 15 
    vTcl:DefineAlias "$site_3_0.lab103" "asiento15" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab104 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 17 
    vTcl:DefineAlias "$site_3_0.lab104" "asiento17" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab105 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 16 
    vTcl:DefineAlias "$site_3_0.lab105" "asiento16" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab106 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 18 
    vTcl:DefineAlias "$site_3_0.lab106" "asiento18" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab107 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 20 
    vTcl:DefineAlias "$site_3_0.lab107" "asiento20" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab108 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 19 
    vTcl:DefineAlias "$site_3_0.lab108" "asiento19" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab44 \
        -activebackground #f9f9f9 -activeforeground black -background #472ce0 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 12 
    vTcl:DefineAlias "$site_3_0.lab44" "asiento12" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra46 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 420 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 253 
    vTcl:DefineAlias "$site_3_0.fra46" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra46
    label $site_4_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black -background #ff8040 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {registro de pasajeros:} 
    vTcl:DefineAlias "$site_4_0.lab47" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent48 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable cedulapasajero -width 10 
    vTcl:DefineAlias "$site_4_0.ent48" "entry_cedula" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Nombre: 
    vTcl:DefineAlias "$site_4_0.lab49" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable nombre_pasajero -width 10 
    vTcl:DefineAlias "$site_4_0.ent50" "entry_nombre" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Cedula: 
    vTcl:DefineAlias "$site_4_0.lab51" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Clase: 
    vTcl:DefineAlias "$site_4_0.lab54" "Label4" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_4_0.tLa55 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Ubicación: 
    vTcl:DefineAlias "$site_4_0.tLa55" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.tBu59 \
        -command registrar_pasajeros -takefocus {} -text {reservar pasaje} 
    vTcl:DefineAlias "$site_4_0.tBu59" "btn_reservarP" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_4_0.tCo44 \
        -values ventana,centro,pasillo -font TkTextFont \
        -textvariable ubicacionP -foreground {} -background #0000ff \
        -takefocus {} 
    vTcl:DefineAlias "$site_4_0.tCo44" "ubicacion_P" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $site_4_0.tCo44
    ttk::combobox $site_4_0.tCo45 \
        -values ejecutiva,economica -font TkTextFont \
        -textvariable clasesvuelos -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_4_0.tCo45" "clases_vuelos" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab47 \
        -in $site_4_0 -x 0 -relx 0.04 -y 0 -rely 0.069 -width 0 \
        -relwidth 0.924 -height 0 -relheight 0.09 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent48 \
        -in $site_4_0 -x 0 -relx 0.277 -y 0 -rely 0.448 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab49 \
        -in $site_4_0 -x 0 -relx 0.353 -y 0 -rely 0.167 -width 0 \
        -relwidth 0.243 -height 0 -relheight 0.09 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent50 \
        -in $site_4_0 -x 0 -relx 0.277 -y 0 -rely 0.241 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab51 \
        -in $site_4_0 -x 0 -relx 0.356 -y 0 -rely 0.345 -width 0 \
        -relwidth 0.206 -height 0 -relheight 0.09 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab54 \
        -in $site_4_0 -x 0 -relx 0.356 -y 0 -rely 0.524 -width 0 \
        -relwidth 0.174 -height 0 -relheight 0.067 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tLa55 \
        -in $site_4_0 -x 0 -relx 0.273 -y 0 -rely 0.667 -width 0 \
        -relwidth 0.336 -height 0 -relheight 0.057 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tBu59 \
        -in $site_4_0 -x 0 -relx 0.553 -y 0 -rely 0.881 -width 109 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.tCo44 \
        -in $site_4_0 -x 0 -relx 0.117 -y 0 -rely 0.762 -width 0 \
        -relwidth 0.574 -height 0 -relheight 0.062 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tCo45 \
        -in $site_4_0 -x 0 -relx 0.117 -y 0 -rely 0.595 -width 0 \
        -relwidth 0.574 -height 0 -relheight 0.062 -anchor nw \
        -bordermode ignore 
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu60 \
        -command buscar_pasajero -takefocus {} -text {Buscar pasajero} 
    vTcl:DefineAlias "$site_3_0.tBu60" "btn_buscarP" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu61 \
        -command eliminar_pasajero -takefocus {} -text {Eliminar pasajero} 
    vTcl:DefineAlias "$site_3_0.tBu61" "btn_eliminarP" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu62 \
        -command porcentaje_ocupacion -takefocus {} \
        -text {Porcentaje ocupacion} 
    vTcl:DefineAlias "$site_3_0.tBu62" "btn_porcentajeO" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab86 \
        -in $site_3_0 -x 0 -relx 0.357 -y 0 -rely 0.064 -width 0 \
        -relwidth 0.047 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab89 \
        -in $site_3_0 -x 0 -relx 0.408 -y 0 -rely 0.061 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab90 \
        -in $site_3_0 -x 0 -relx 0.55 -y 0 -rely 0.061 -width 0 \
        -relwidth 0.047 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab91 \
        -in $site_3_0 -x 0 -relx 0.607 -y 0 -rely 0.061 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab92 \
        -in $site_3_0 -x 0 -relx 0.551 -y 0 -rely 0.127 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab93 \
        -in $site_3_0 -x 0 -relx 0.359 -y 0 -rely 0.123 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab94 \
        -in $site_3_0 -x 0 -relx 0.408 -y 0 -rely 0.123 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab96 \
        -in $site_3_0 -x 0 -relx 0.607 -y 0 -rely 0.123 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab97 \
        -in $site_3_0 -x 0 -relx 0.303 -y 0 -rely 0.205 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab98 \
        -in $site_3_0 -x 0 -relx 0.36 -y 0 -rely 0.205 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab99 \
        -in $site_3_0 -x 0 -relx 0.417 -y 0 -rely 0.205 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab100 \
        -in $site_3_0 -x 0 -relx 0.597 -y 0 -rely 0.205 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab102 \
        -in $site_3_0 -x 0 -relx 0.654 -y 0 -rely 0.205 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab103 \
        -in $site_3_0 -x 0 -relx 0.303 -y 0 -rely 0.287 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab104 \
        -in $site_3_0 -x 0 -relx 0.417 -y 0 -rely 0.287 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab105 \
        -in $site_3_0 -x 0 -relx 0.36 -y 0 -rely 0.287 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab106 \
        -in $site_3_0 -x 0 -relx 0.54 -y 0 -rely 0.287 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab107 \
        -in $site_3_0 -x 0 -relx 0.654 -y 0 -rely 0.287 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab108 \
        -in $site_3_0 -x 0 -relx 0.597 -y 0 -rely 0.287 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab44 \
        -in $site_3_0 -x 0 -relx 0.54 -y 0 -rely 0.205 -width 0 \
        -relwidth 0.045 -height 0 -relheight 0.053 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra46 \
        -in $site_3_0 -x 0 -relx 0.047 -y 0 -rely 0.021 -width 0 \
        -relwidth 0.24 -height 0 -relheight 0.897 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu60 \
        -in $site_3_0 -x 0 -relx 0.37 -y 0 -rely 0.876 -width 114 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu61 \
        -in $site_3_0 -x 0 -relx 0.502 -y 0 -rely 0.876 -width 125 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu62 \
        -in $site_3_0 -x 0 -relx 0.638 -y 0 -rely 0.876 -width 168 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    vTcl:copy_lock $top.can84
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can84 \
        -in $top -x 0 -relx 0.027 -y 0 -rely 0.02 -width 0 -relwidth 0.953 \
        -height 0 -relheight 0.936 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top43 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

