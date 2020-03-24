#!/bin/bash

IN_PATH=/Volumes/git/projects/personal/pyDF/raspi_df/assets/ui/
OUT_PATH=/Volumes/git/projects/personal/pyDF/raspi_df/assets/ui/

X=160
Y=40


# Exit Button
egg-texture-cards -o ${OUT_PATH}exit_button.egg \
    -aniso 16 ${IN_PATH}btn_idle_exit.png ${IN_PATH}btn_over_exit.png \
    -p $X,$Y -minf "mipmap" -magf "linear" -ql "best"

egg2bam -ps rel -o ${OUT_PATH}exit_button.bam ${IN_PATH}exit_button.egg

# Options Button
egg-texture-cards -o ${OUT_PATH}options_button.egg \
    -aniso 16 ${IN_PATH}btn_idle_options.png ${IN_PATH}btn_over_options.png \
    -p $X,$Y -minf "mipmap" -magf "linear" -ql "best"

egg2bam -ps rel -o ${OUT_PATH}options_button.bam ${IN_PATH}options_button.egg

# Menu bar
egg-texture-cards -o ${OUT_PATH}menu_bar.egg \
    -aniso 16 ${IN_PATH}bar_main_menu.png \
    -minf "mipmap" -magf "linear" -ql "best"

egg2bam -ps rel -o ${OUT_PATH}menu_bar.bam ${IN_PATH}menu_bar.egg