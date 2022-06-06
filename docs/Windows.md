Install on Windows
=========================

Install TeX Live
--------------------------
- https://www.tug.org/texlive/windows.html
로 가서 Easy install 항목의 install-tl-windows.exe 받아서 설치
- 1시간 넘게 걸리니까 설치하면서 다음 항목으로 ㄱ

Install Git
---------------
http://git-scm.com/download/win
들어가서 가장 최근 거 받아서 설치

Install gVim
---------------------------
- https://github.com/vim/vim-win32-installer/releases
로 가서 Files 항목의 64-bit installer 받아서 설치
- 설치하면 gVim과 gVim-Easy가 설치되는데 gVim-Easy 관리자 권한으로 실행
- 편집 - 글꼴 고르기 로 가서 원하는 글꼴 설정
- `<Control-R>=&guifont` 치고 엔터 치면 `Fixedsys:h15:cHANGEUL:qDRAFT` 같은 거 나올 거임. 그거 복사하기
- 편집 - 시작 설정 들어가면 위쪽 절반에 새로운 문서가 나올 거임. 그 문서 마지막 줄로 가서 `set guifont = <복사한 내용>` 입력하고 파일 - 저장.
<!--
- `:set guifont?` 치고 엔터 치면 `guifont=Fixedsys:h20:cHANGEUL:qDRAFT` 같은 거 나올 거임. 그거 복사해서
-->
- 이쯤에서 gVim-Easy 끄고 gVim으로 돌아와서 https://www.youtube.com/watch?v=GWo_MxMlJJ4 보면서 vim 기본 익히면 좋을 거임.
    - 영상에 나오는 단축키들 부연설명
    - i : insert
    - a : append
    - y : yank(복사)
    - p : paste
    - d : delete

Install vim-plug
------------------------
- https://github.com/junegunn/vim-plug
로 가서 Installation - Vim (Neovim 아니니까 주의!) - Windows(PowerShell) 항목의 코드 복사 후 powershell 열어서 붙여넣고 실행

Setup Vim
------------------------
- gVim 관리자 권한으로 실행한 후, 편집 - 시작 설정 들어가서 맨 밑에 아래 내용 붙여넣기.

<!--
https://www.shortcutfoo.com/blog/top-50-vim-configuration-options/
-->
```vim
set autoindent " New lines inherit the indentation of previous lines
set expandtab " Convert tabs to spaces
filetype indent on " Enable indentation rules that are file-type specific
set shiftround " When shifting lines, round the indentation to the nearest multiple of "shiftwidth"
set shiftwidth=4 " When shifting(<<, >>), indent using four spaces
set smarttab " Insert "tabstop" number of spaces when the "tab" key is pressed
set tabstop=4 " Indent using 4 spaces
set softtabstop=4 " 

set hlsearch " Enable search highlighting
set ignorecase " Ignore case when searching
set incsearch " Incremental search that shows partial matches
set smartcase " Automatically switch search to case-sensitive when search query contains an uppercase letter

set laststatus=2 " Always display the status bar
set ruler " Always show cursor position
set wildmenu " Display command line's tab complete options as a menu
set cursorline " Highlight the line currently under cursor
set number " Show line numbers on the sidebar
set relativenumber " Show line number on the current line and relative numbers on all other lines
set noerrorbells " Disable beep on errors
set visualbell " Flash the screen instead of beeping on errors
set title " Set the window's title, reflecting the file currently being edited

set backspace=indent,eol,start " Allow backspacing over indentation, line breaks and insertion start
set history=1000 " Increase the undo limit


call plug#begin()

Plug 'lervag/vimtex'
let g:vimtex_view_general_options = '-reuse-instance @pdf'
let g:vimtex_compiler_latexmk = {
        \ 'executable' : 'latexmk',
        \ 'options' : [
        \   '-xelatex',
        \   '-file-line-error',
        \   '-synctex=1',
        \   '-interaction=nonstopmode',
        \ ],
        \}
let g:vimtex_view_general_viewer = 'sumatraPDF'  " for Windows
" let g:vimtex_view_general_viewer = 'skim'  " for Mac

Plug 'SirVer/ultisnips'
let g:python3_host_prog = '/usr/bin/python3'

let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"

let g:UltiSnipsEditSplit="vertical"

let g:UltiSnipsSnippetDirectories=["UltiSnips", "my_snippets"]

Plug 'piaxydls002/LaTeX-snippets'

call plug#end()
```
