org 0100h

MVI C,93H
CALL 5

mvi a,0h
MVI B,255
COUNTER:
    MVI C,255
    COUNTER$INNER$1:
        MVI D,255
        COUNTER$INNER$2:
            MVI E,255
            COUNTER$INNER$3:
                add a
                DCR E
                JNZ COUNTER$INNER$3
            DCR D
            JNZ COUNTER$INNER$2
        DCR C
        JNZ COUNTER$INNER$1
    mvi a,31h
    out 01h
    DCR B
    JNZ COUNTER

MVI A,21h
out 01h

ret
end
