Install on Windows
=========================

Install TeX Live
--------------------------
- https://www.tug.org/texlive/windows.html
로 가서 Easy install 항목의 install-tl-windows.exe 받아서 설치
- 1시간 넘게 걸리니까 설치하면서 다음 항목으로 ㄱ

Install SumatraPDF
----------------------------
- https://www.sumatrapdfreader.org/download-free-pdf-viewer 가서 64-bit 버전 다운받아 설치
    - 설치위치 기록 (아마 `C:\Users\(username)\AppData\Local\SumatraPDF)`
- 앞에서 기록한 설치위치를 복사하고, 제어판이나 시작 메뉴에서 '계정의 환경 변수 편집' 검색해서 열기
- 사용자 변수에서 Path 더블클릭하고 새로 만들기 - 복사한 설치위치 붙여넣고 저장

Install Python
---------------------
<!--
:version
-->
- https://www.python.org/downloads/
에서 가장 최신 버전 받아서 설치
    - Add to PATH 옵션에 체크

Install Git
---------------
- http://git-scm.com/download/win
들어가서 가장 최근 거 받아서 설치
    - 중간에 Adjusting the name of the initial branch 옵션에서는 Let Git decide 말고 Override the default branch name for new repositories 선택, main으로 설정하고 진행

Install gVim
---------------------------
- https://github.com/vim/vim-win32-installer/releases
로 가서 Files 항목의 64-bit installer 받아서 설치
- 설치하면 gVim과 gVim-Easy가 설치되는데 gVim-Easy 관리자 권한으로 실행
- 편집 - 글꼴 고르기 로 가서 원하는 글꼴 설정
- `<Control-R>=&guifont` 치고 엔터 치면 `돋움체:h16:cANSI:qDRAFT` 같은 거 나올 거임. 그거 복사하기
- 편집 - 시작 설정 들어가면 위쪽 절반에 새로운 문서가 나올 거임. 그 문서 마지막 줄로 가서 `set guifont=<복사한 내용>` 입력(= 주위로 공백 X)하고 파일 - 저장.
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
- gVim 관리자 권한으로 실행한 후, 편집 - 시작 설정 들어가서 맨 밑에 아래 내용 붙여넣고 저장.

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
let g:vimtex_imaps_enabled = 0
let g:vimtex_compiler_latexmk_engines = {
        \ '_' : '-xelatex',
        \}

Plug 'SirVer/ultisnips'

let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"

let g:UltiSnipsEditSplit="vertical"

let g:UltiSnipsSnippetDirectories=["UltiSnips", "my_snippets"]

Plug 'piaxydls002/LaTeX-snippets'

call plug#end()
```

Install Plugins
------------------
- Vim 열어서 :PlugInstall 치고 엔터. 창 나오는 건 :q로 그냥 끄면 됨.
- 나중에 업데이트는 :PlugUpdate
- `C:\Users\(username)`에 `.latexmkrc` 라는 이름의 파일 만들어주고 열어서 `$xelatex = "xelatex -file-line-error -synctex=1 -interaction=nonstopmode -recorder %S"` 적고 저장
- SumatraPDF 열어서 설정 - 옵션 - 명령줄 역방향 탐색 설정에 `gvim --servername GVIM --remote-send "<C-\><C-n>:drop %f<CR>:%l<CR>:normal! zzzv<CR>:execute 'drop ' . fnameescape('%f')<CR>:%l<CR>:normal! zzzv<CR>:call remote_foreground('GVIM')<CR><CR>"` 

재부팅
----------
- 그냥 한번 해주기

시작!
-------
- 샘플 텍 파일 test.tex 만듬. 연결 프로그램은 Vim으로 해서 열어주기
- 열어서 testdoc이라고 입력
- group 치고 tab 누르고 다시 tab tab 후 시키는 대로
- :w로 저장한 후에 \ll 눌러서 컴파일
- \lk나 \ll 다시 눌러서 컴파일 중지, \lc로 파일 청소
- 컴파일 중이면 저장할 때마다 자동으로 업데이트됨.
