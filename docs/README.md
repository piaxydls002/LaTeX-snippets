User Guide(Windows)
===================

Install Ubuntu on Windows
-------------------------
- 관리자 권한으로 명령프롬프트/PowerShell 실행 후
```powershell
wsl --install
```
입력 후 재부팅
- Ubuntu 터미널에서 username/password 설정 후
```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install latexmk
sudo apt install python3-pip
pip install neovim
```
해주기

<!--
https://docs.microsoft.com/ko-kr/windows/wsl/install

Error Messages
--------------
+ `WSL optional component is not enabled`
  - 제어판-프로그램-windows 기능 켜기/끄기-Linux용 Windows 하위 시스템 체크 후 확인 및 재부팅
+ `Error: 0x800701bc WSL 2?????????https://aka.ms/wsl2kernel??????`
  - https://docs.microsoft.com/ko-kr/windows/wsl/install-manual 의 4번 항목에 있는 Linux 커널 업데이트 패키지를 다운받아 설치
-->

Install SumatraPDF
-------------------
- https://www.sumatrapdfreader.org/download-free-pdf-viewer 가서 다운받아 설치
- 설치 폴더(아마 `C:\Users\(사용자명)\AppData\Local\SumatraPDF`) 가서 SumatraPDF.exe의 복사본을 만들고 .exe를 제거한 SumatraPDF로 파일명 변경
- 설치 폴더 경로 복사
- Win+S에 path 검색 - 시스템 환경 변수 편집 - 환경 변수 - [~에 대한 사용자 변수] 중 Path 더블클릭 - 새로 만들기 - 아까 복사한 경로 붙여넣기 - 확인x3



Install neovim
--------------
- https://github.com/neovim/neovim/releases/latest
에서 제일 아래로 내려가서 nvim-linux64.deb 우클릭 후 링크 주소 복사
```
wget (방금 복사한 링크)
sudo apt install ./nvim-linux64.deb
```
입력 후 `nvim` 치면 실행됨

Install TeX Live
----------------
```sh
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xvf install-tl-unx.tar.gz
```
`ls`로 install-tl-20220418 같은 폴더 있는 거 확인
```sh
cd install-tl-202*****(아까 확인한 폴더명)
sudo perl install-tl
i
```
오래 걸림
- 다 끝나면 ~/.bashrc 열어서 맨 마지막에
```sh
export MANPATH="/usr/local/texlive/2022/texmf-dist/doc/man:$MANPATH"
export INFOPATH="/usr/local/texlive/2022/texmf-dist/doc/info:$INFOPATH"
export PATH="/usr/local/texlive/2022/bin/x86_64-linux:$PATH"
```
추가해주기

Install neovim plugins
----------------------
- vim-plug
```sh
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

- ~/.config/nvim 폴더에 init.vim 생성하기
```sh
mkdir {.config,.config/nvim}
cd .config/nvim
nvim init.vim
```

i 쳐서 입력모드로 들어간 뒤 다음 내용 붙여넣고(우클릭) Esc 후 :wq 로 저장 후 종료
```vim
:set number " show line number
:set relativenumber " show relative line number

:set autoindent " auto indent new line
:set expandtab " change tab to space
:set smarttab
:set tabstop=4 " tab = 4 space
:set shiftwidth=4 " <<, >> changes 4 space
:set softtabstop=4 " 4 space == tab


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
let g:vimtex_view_general_viewer = 'sumatraPDF'
    
Plug 'SirVer/ultisnips'
let g:python3_host_prog = '/usr/bin/python3'

let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"

let g:UltiSnipsEditSplit="vertical"

let g:UltiSnipsSnippetDirectories=["my_snippets", "TeX-snippets"]

Plug 'piaxydls002/TeX-snippets', {'dir': '~/.config/nvim/TeX-snippets'}

call plug#end()
```

다시 nvim 들어가서 `:PlugInstall` 해주면 플러그인들 설치 완료

- 테스트
```sh
nvim test.tex
```
```vim
template [tab]
im [tab]
//3[tab]5[tab]+nr3[tab]2
```
Esc누르고 :w로 저장, \ll 쳐서 컴파일되는 거 확인.(이러면 저장할 때마다 다시 컴파일됨) \lk로 컴파일 종료, \lc로 파일들 청소
