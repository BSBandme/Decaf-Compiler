.data

	sap: .space 4

.text

l5_print_Out_begin:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
l6_print_Out_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

l7_print_Out_begin:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
l8_print_Out_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

l9_print_Out_begin:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
l10_print_Out_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

l11_print_Out_begin:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
l12_print_Out_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

l13_fib_foo_begin:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
	li $t0,2
	sle $t0,$a1,$t0
	beqz $t0,l22_IfElseStmtStart
l20_IfStmtStart:
	li $t0,1
	move $v0,$t0
	j l14_fib_foo_end
l25_end_return:
	j l24_IfOverallEnd
l22_IfElseStmtStart:
l24_IfOverallEnd:
	move $t1,$a0
	li $t0,1
	sub $t0,$a1,$t0
l26_method_call:
	subu $sp,$sp,4
	sw $a0,0($sp)
	subu $sp,$sp,4
	sw $a1,0($sp)
	subu $sp,$sp,4
	sw $a2,0($sp)
	subu $sp,$sp,4
	sw $a3,0($sp)
	subu $sp,$sp,4
	sw $t0,0($sp)
	subu $sp,$sp,4
	sw $t1,0($sp)
	subu $sp,$sp,4
	sw $t2,0($sp)
	subu $sp,$sp,4
	sw $t3,0($sp)
	subu $sp,$sp,4
	sw $t4,0($sp)
	subu $sp,$sp,4
	sw $t5,0($sp)
	subu $sp,$sp,4
	sw $t6,0($sp)
	subu $sp,$sp,4
	sw $t7,0($sp)
	subu $sp,$sp,4
	sw $t8,0($sp)
	subu $sp,$sp,4
	sw $t9,0($sp)
	move $a0,$t1
	move $a1,$t0
	jal l13_fib_foo_begin
	lw $t9,0($sp)
	addu $sp,$sp,4
	lw $t8,0($sp)
	addu $sp,$sp,4
	lw $t7,0($sp)
	addu $sp,$sp,4
	lw $t6,0($sp)
	addu $sp,$sp,4
	lw $t5,0($sp)
	addu $sp,$sp,4
	lw $t4,0($sp)
	addu $sp,$sp,4
	lw $t3,0($sp)
	addu $sp,$sp,4
	lw $t2,0($sp)
	addu $sp,$sp,4
	lw $t1,0($sp)
	addu $sp,$sp,4
	lw $t0,0($sp)
	addu $sp,$sp,4
	lw $a3,0($sp)
	addu $sp,$sp,4
	lw $a2,0($sp)
	addu $sp,$sp,4
	lw $a1,0($sp)
	addu $sp,$sp,4
	lw $a0,0($sp)
	addu $sp,$sp,4
	move $t1,$v0
l27_method_call_end:
	move $t2,$a0
	li $t0,2
	sub $t0,$a1,$t0
l28_method_call:
	subu $sp,$sp,4
	sw $a0,0($sp)
	subu $sp,$sp,4
	sw $a1,0($sp)
	subu $sp,$sp,4
	sw $a2,0($sp)
	subu $sp,$sp,4
	sw $a3,0($sp)
	subu $sp,$sp,4
	sw $t0,0($sp)
	subu $sp,$sp,4
	sw $t1,0($sp)
	subu $sp,$sp,4
	sw $t2,0($sp)
	subu $sp,$sp,4
	sw $t3,0($sp)
	subu $sp,$sp,4
	sw $t4,0($sp)
	subu $sp,$sp,4
	sw $t5,0($sp)
	subu $sp,$sp,4
	sw $t6,0($sp)
	subu $sp,$sp,4
	sw $t7,0($sp)
	subu $sp,$sp,4
	sw $t8,0($sp)
	subu $sp,$sp,4
	sw $t9,0($sp)
	move $a0,$t2
	move $a1,$t0
	jal l13_fib_foo_begin
	lw $t9,0($sp)
	addu $sp,$sp,4
	lw $t8,0($sp)
	addu $sp,$sp,4
	lw $t7,0($sp)
	addu $sp,$sp,4
	lw $t6,0($sp)
	addu $sp,$sp,4
	lw $t5,0($sp)
	addu $sp,$sp,4
	lw $t4,0($sp)
	addu $sp,$sp,4
	lw $t3,0($sp)
	addu $sp,$sp,4
	lw $t2,0($sp)
	addu $sp,$sp,4
	lw $t1,0($sp)
	addu $sp,$sp,4
	lw $t0,0($sp)
	addu $sp,$sp,4
	lw $a3,0($sp)
	addu $sp,$sp,4
	lw $a2,0($sp)
	addu $sp,$sp,4
	lw $a1,0($sp)
	addu $sp,$sp,4
	lw $a0,0($sp)
	addu $sp,$sp,4
	move $t0,$v0
l29_method_call_end:
	add $t0,$t1,$t0
	move $v0,$t0
	j l14_fib_foo_end
l30_end_return:
l14_fib_foo_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

main:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
	li $t0,0
	li $t2,2
	mul $t0,$t0,4
	la $v0,sap
	add $v0,$v0,$t0
	sw $t2,0($v0)
	div $t0,$t0,4
	li $t0,0
	move $t2,$t0
l31_while_start:
	li $t0,10
	slt $t0,$t2,$t0
	beqz $t0,l36_while_end
l34_while_body_start:
	li $t0,1
	add $t0,$t2,$t0
	move $t2,$t0
	j l31_while_start
l36_while_end:
	li $t0,0
	move $t2,$t0
l40_for_condStart:
	li $t0,10
	slt $t0,$t2,$t0
	beqz $t0,l46_for_end
l42_for_bodyStart:
	add $t0,$t1,$t2
	move $t1,$t0
l44_for_updateStart:
	li $t0,1
	add $t2,$t2,$t0
	j l40_for_condStart
l46_for_end:
	li $t0,3
	move $t1,$t0
	li $t0,3
	slt $t0,$t2,$t0
	beqz $t0,l50_IfElseStmtStart
l48_IfStmtStart:
	li $t0,2
	mul $t0,$t1,$t0
	move $t1,$t0
	j l52_IfOverallEnd
l50_IfElseStmtStart:
	li $t0,2
	div $t0,$t1,$t0
	move $t1,$t0
l52_IfOverallEnd:
	move $t0,$a0
	li $t1,10
l53_method_call:
	subu $sp,$sp,4
	sw $a0,0($sp)
	subu $sp,$sp,4
	sw $a1,0($sp)
	subu $sp,$sp,4
	sw $a2,0($sp)
	subu $sp,$sp,4
	sw $a3,0($sp)
	subu $sp,$sp,4
	sw $t0,0($sp)
	subu $sp,$sp,4
	sw $t1,0($sp)
	subu $sp,$sp,4
	sw $t2,0($sp)
	subu $sp,$sp,4
	sw $t3,0($sp)
	subu $sp,$sp,4
	sw $t4,0($sp)
	subu $sp,$sp,4
	sw $t5,0($sp)
	subu $sp,$sp,4
	sw $t6,0($sp)
	subu $sp,$sp,4
	sw $t7,0($sp)
	subu $sp,$sp,4
	sw $t8,0($sp)
	subu $sp,$sp,4
	sw $t9,0($sp)
	move $a0,$t0
	move $a1,$t1
	jal l13_fib_foo_begin
	lw $t9,0($sp)
	addu $sp,$sp,4
	lw $t8,0($sp)
	addu $sp,$sp,4
	lw $t7,0($sp)
	addu $sp,$sp,4
	lw $t6,0($sp)
	addu $sp,$sp,4
	lw $t5,0($sp)
	addu $sp,$sp,4
	lw $t4,0($sp)
	addu $sp,$sp,4
	lw $t3,0($sp)
	addu $sp,$sp,4
	lw $t2,0($sp)
	addu $sp,$sp,4
	lw $t1,0($sp)
	addu $sp,$sp,4
	lw $t0,0($sp)
	addu $sp,$sp,4
	lw $a3,0($sp)
	addu $sp,$sp,4
	lw $a2,0($sp)
	addu $sp,$sp,4
	lw $a1,0($sp)
	addu $sp,$sp,4
	lw $a0,0($sp)
	addu $sp,$sp,4
	move $t0,$v0
l54_method_call_end:
	move $t2,$t0
	j l16_main_foo_end
l55_end_return:
l16_main_foo_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

l17_C_1:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

l1_scan_int_In_begin:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
l2_scan_int_In_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

l3_scan_float_In_begin:
	subu $sp,$sp,8
	sw $ra,4($sp)
	sw $fp,0($sp)
	addu $fp,$sp,8
l4_scan_float_In_end:
	lw $ra,4($sp)
	lw $fp,0($sp)
	addu $sp,$sp,8
	jr $ra

