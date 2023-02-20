seção .text
_início global
_começar:
    mov edx, apenas
    mov ecx,msg
    mov     ebx,1
    mover eax,4
    int 0x80
    mover eax,1
    int 0x80
seção .data
msg db 'Olá mundo',0xa
apenas equ $ - msg