	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 3
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #144                    ; =144
	stp	x29, x30, [sp, #128]            ; 16-byte Folded Spill
	add	x29, sp, #128                   ; =128
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	wzr, [x29, #-4]
	stur	w0, [x29, #-8]
	stur	x1, [x29, #-16]
	ldur	w8, [x29, #-8]
	subs	w8, w8, #4                      ; =4
	b.eq	LBB0_2
; %bb.1:
	ldur	x8, [x29, #-16]
	ldr	x8, [x8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	mov	w8, #-1
	stur	w8, [x29, #-4]
	b	LBB0_3
LBB0_2:
	ldur	x8, [x29, #-16]
	ldr	x8, [x8, #8]
	stur	x8, [x29, #-24]
	ldur	x8, [x29, #-16]
	ldr	x8, [x8, #16]
	stur	x8, [x29, #-32]
	ldur	x8, [x29, #-16]
	ldr	x8, [x8, #24]
	sub	x9, x29, #40                    ; =40
	str	x9, [sp, #16]                   ; 8-byte Folded Spill
	stur	x8, [x29, #-40]
	sub	x1, x29, #48                    ; =48
	str	x1, [sp, #24]                   ; 8-byte Folded Spill
	adrp	x8, l_.str.1@PAGE
	add	x8, x8, l_.str.1@PAGEOFF
	stur	x8, [x29, #-48]
	sub	x8, x29, #56                    ; =56
	str	x8, [sp, #40]                   ; 8-byte Folded Spill
	adrp	x8, l_.str.2@PAGE
	add	x8, x8, l_.str.2@PAGEOFF
	stur	x8, [x29, #-56]
	ldur	x0, [x29, #-32]
	mov	x2, #1
	str	x2, [sp, #32]                   ; 8-byte Folded Spill
	mov	x3, #-1
	str	x3, [sp, #56]                   ; 8-byte Folded Spill
	bl	___strncat_chk
	ldr	x1, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x3, [sp, #56]                   ; 8-byte Folded Reload
	ldur	x8, [x29, #-32]
	str	x8, [sp, #64]
	ldr	x0, [sp, #64]
	mov	x2, #200
	str	x2, [sp, #48]                   ; 8-byte Folded Spill
	bl	___strncat_chk
	ldr	x1, [sp, #24]                   ; 8-byte Folded Reload
	ldr	x2, [sp, #32]                   ; 8-byte Folded Reload
	ldr	x3, [sp, #56]                   ; 8-byte Folded Reload
	ldr	x0, [sp, #64]
	bl	___strncat_chk
	ldr	x1, [sp, #40]                   ; 8-byte Folded Reload
	ldr	x2, [sp, #48]                   ; 8-byte Folded Reload
	ldr	x3, [sp, #56]                   ; 8-byte Folded Reload
	ldr	x0, [sp, #64]
	bl	___strncat_chk
	ldr	x8, [sp, #64]
	adrp	x0, l_.str.3@PAGE
	add	x0, x0, l_.str.3@PAGEOFF
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	stur	wzr, [x29, #-4]
LBB0_3:
	ldur	w0, [x29, #-4]
	ldp	x29, x30, [sp, #128]            ; 16-byte Folded Reload
	add	sp, sp, #144                    ; =144
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"Invalid arguments - %s <host> <GET|POST> <path>\n"

l_.str.1:                               ; @.str.1
	.asciz	" "

l_.str.2:                               ; @.str.2
	.asciz	"HTTP/1.0\r\n\r\n"

l_.str.3:                               ; @.str.3
	.asciz	"%s"

.subsections_via_symbols
