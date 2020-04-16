#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Apr 14, 2020 12:23:14 PM -03  platform: Windows NT
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
        -menu {{}} -relief raised -background $vTcl(actual_gui_bg) \
        -highlightbackground #f0f0f0f0f0f0 -highlightcolor #646464646464 
    wm focusmodel $top passive
    wm geometry $top 271x650+1031+149
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
    vTcl:DefineAlias "$top" "costeDeViaje" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::label $top.tLa46 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Viajeros: 
    vTcl:DefineAlias "$top.tLa46" "label1" vTcl:WidgetProc "costeDeViaje" 1
    spinbox $top.spi48 \
        -activebackground #f9f9f9 -background white -buttonbackground #d9d9d9 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground black \
        -from 1.0 -highlightbackground black -highlightcolor black \
        -increment 1.0 -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable cantidadViajeros -to 100.0 
    vTcl:DefineAlias "$top.spi48" "Spinbox1" vTcl:WidgetProc "costeDeViaje" 1
    label $top.lab50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Clase: 
    vTcl:DefineAlias "$top.lab50" "Label2" vTcl:WidgetProc "costeDeViaje" 1
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $top.tRa53 \
        -variable rButton -value Lujo -takefocus {} -text Lujo 
    vTcl:DefineAlias "$top.tRa53" "radioButtonLujo" vTcl:WidgetProc "costeDeViaje" 1
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $top.tRa54 \
        -variable rButton -value Turista -takefocus {} -text Turista 
    vTcl:DefineAlias "$top.tRa54" "radioButton" vTcl:WidgetProc "costeDeViaje" 1
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $top.tRa55 \
        -variable rButton -value Primera -takefocus {} -text Primera 
    vTcl:DefineAlias "$top.tRa55" "radioButtonPrimera" vTcl:WidgetProc "costeDeViaje" 1
    ttk::label $top.tLa56 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {Distancia (Kilometros):} 
    vTcl:DefineAlias "$top.tLa56" "TLabel2" vTcl:WidgetProc "costeDeViaje" 1
    ttk::entry $top.tEn57 \
        -font TkTextFont -textvariable distancia -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$top.tEn57" "entryDistancia" vTcl:WidgetProc "costeDeViaje" 1
    ttk::label $top.tLa58 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Precio: 
    vTcl:DefineAlias "$top.tLa58" "TLabel3" vTcl:WidgetProc "costeDeViaje" 1
    ttk::entry $top.tEn59 \
        -font TkTextFont -textvariable precio -foreground {} -background {} \
        -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$top.tEn59" "entryPrecio" vTcl:WidgetProc "costeDeViaje" 1
    ttk::label $top.tLa60 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {A Pagar (euros):} 
    vTcl:DefineAlias "$top.tLa60" "TLabel4" vTcl:WidgetProc "costeDeViaje" 1
    ttk::label $top.tLa61 \
        -background #000000 -foreground #ffff00 -font TkDefaultFont \
        -relief sunken -anchor w -justify right -textvariable totalPagar 
    vTcl:DefineAlias "$top.tLa61" "montoPagar" vTcl:WidgetProc "costeDeViaje" 1
    ttk::separator $top.tSe62
    vTcl:DefineAlias "$top.tSe62" "TSeparator1" vTcl:WidgetProc "costeDeViaje" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu45 \
        -command salir -takefocus {} -text Salir 
    vTcl:DefineAlias "$top.tBu45" "buttonSalir" vTcl:WidgetProc "costeDeViaje" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu47 \
        -command calculoImporte -takefocus {} -text Calcular 
    vTcl:DefineAlias "$top.tBu47" "buttonCalcular" vTcl:WidgetProc "costeDeViaje" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $top.tCh50 \
        -variable check -takefocus {} -text {Ida y Vuelta} 
    vTcl:DefineAlias "$top.tCh50" "checkButton" vTcl:WidgetProc "costeDeViaje" 1
    canvas $top.can44 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 103 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 233 
    vTcl:DefineAlias "$top.can44" "Canvas1" vTcl:WidgetProc "costeDeViaje" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tLa46 \
        -in $top -x 0 -relx 0.037 -y 0 -rely 0.185 -width 0 -relwidth 0.221 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
    place $top.spi48 \
        -in $top -x 0 -relx 0.074 -y 0 -rely 0.231 -width 0 -relwidth 0.871 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.037 -y 0 -rely 0.369 -width 0 -relwidth 0.155 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.tRa53 \
        -in $top -x 0 -relx 0.111 -y 0 -rely 0.508 -width 0 -relwidth 0.258 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.tRa54 \
        -in $top -x 0 -relx 0.111 -y 0 -rely 0.415 -width 0 -relwidth 0.258 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.tRa55 \
        -in $top -x 0 -relx 0.111 -y 0 -rely 0.462 -width 0 -relwidth 0.295 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.tLa56 \
        -in $top -x 0 -relx 0.037 -y 0 -rely 0.554 -width 0 -relwidth 0.609 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
    place $top.tEn57 \
        -in $top -x 0 -relx 0.074 -y 0 -rely 0.6 -width 0 -relwidth 0.871 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.tLa58 \
        -in $top -x 0 -relx 0.037 -y 0 -rely 0.662 -width 0 -relwidth 0.203 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
    place $top.tEn59 \
        -in $top -x 0 -relx 0.074 -y 0 -rely 0.708 -width 0 -relwidth 0.871 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.tLa60 \
        -in $top -x 0 -relx 0.037 -y 0 -rely 0.769 -width 0 -relwidth 0.424 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
    place $top.tLa61 \
        -in $top -x 0 -relx 0.074 -y 0 -rely 0.815 -width 0 -relwidth 0.867 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.tSe62 \
        -in $top -x 0 -relx 0.037 -y 0 -rely 0.892 -width 0 -relwidth 0.923 \
        -height 0 -relheight 0.003 -anchor nw -bordermode inside 
    place $top.tBu45 \
        -in $top -x 0 -relx 0.554 -y 0 -rely 0.908 -width 98 -relwidth 0 \
        -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tBu47 \
        -in $top -x 0 -relx 0.074 -y 0 -rely 0.908 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCh50 \
        -in $top -x 0 -relx 0.111 -y 0 -rely 0.323 -height 0 -relheight 0.04 \
        -anchor nw -bordermode ignore 
    place $top.can44 \
        -in $top -x 0 -relx 0.074 -y 0 -rely 0.015 -width 0 -relwidth 0.86 \
        -height 0 -relheight 0.158 -anchor nw -bordermode ignore 
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

