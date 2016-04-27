set fileencodings=utf-8
set fileencoding=utf-8
set encoding=utf-8
set termencoding=utf-8

set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set cindent 
syntax on

set cinoptions={0,1s,t0,n-2,p2s,(03s,=.5s,>1s,=1s,:1s
set backspace=indent,eol,start


if &term=="xterm"        
	set t_Co=8        
	set t_Sb=^[[4%dm        
	set t_Sf=^[[3%dm
endif

au bufwritepost ~/.vimrc  :source ~/.vimrc 	" The config takes effect,
						" immediately :w .vimrc

let mapleader=","	" set mapleader
map <leader>ev	:edit ~/.vimrc<cr>
map <leader>wk  <C-w><C-k>

set nu			" Show number of line

filetype plugin on 

set nocompatible	" Use Vim defaults (much better!)

let g:doxygenToolkit_briefTag_funcName="yes"
let g:DoxygenToolkit_briefTag_pre="@brief " 
let g:DoxygenToolkit_paramTag_pre="@param " 
let g:DoxygenToolkit_returnTag="@return " 
map <leader>df :Dox<cr>


set bs=2		" allow backspacing over everything in insert mode
"set ai			" always set autoindenting on
"set backup		" keep a backup file
set viminfo='20,\"50	" read/write a .viminfo file, don't store more
			" than 50 lines of registers
set history=50		" keep 50 lines of command line history
set ruler		" show the cursor position all the time

autocmd FileType h,c,cpp,python,sh set shiftwidth=4 expandtab ts=4

syntax on
set hlsearch
set smartcase
set showmatch
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif

"set t_Co=256
"set showmode
"set showcmd
"set title
"set laststatus=2
"set report=0
"set nowrap
"set novisualbell

"if has("statusline")
"	set statusline=%F%m%r%h%w\ %=[FORMAT=%{&ff}]\ %{\"[\".(&fenc==\"\"?&enc:&fenc).((exists(\"+bomb\")\ &&\ &bomb)?\",B\":\"\").\"]\"}\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")}
"endif
