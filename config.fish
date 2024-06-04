# General Configuration
set fish_greeting

# Starship Configuration
starship init fish | source

# One Dark Configuration
set -l onedark_black 282c34
set -l onedark_grey 5c6370
set -l onedark_white abb2bf
set -l onedark_red e06c75
set -l onedark_blue 61afef
set -l onedark_cyan 56b6c2
set -l onedark_green 98c379
set -l onedark_purple c678dd
set -l onedark_orange d19a66
set -l onedark_yellow e5c07b

# Colours Configuration
set fish_color_normal $onedark_white
set fish_color_command $onedark_purple --bold
set fish_color_quote $onedark_green
set fish_color_redirection $onedark_cyan
set fish_color_end $onedark_white --bold
set fish_color_error $onedark_red --bold
set fish_color_param $onedark_red
set fish_color_valid_path --underline
set fish_color_option $onedark_orange
set fish_color_comment $onedark_grey --italics
set fish_color_operator $onedark_purple
set fish_color_escape $onedark_cyan
set fish_color_autosuggestion $onedark_white
set fish_color_cancel $onedark_grey
set fish_color_history_current $onedark_cyan

set fish_pager_color_progress $onedark_white --bold
set fish_pager_color_completion $onedark_white
set fish_pager_color_prefix $onedark_green
set fish_pager_color_description $onedark_yellow
