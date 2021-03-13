-- https://programmers.co.kr/learn/courses/30/lessons/59043

SELECT INS.ANIMAL_ID, INS.NAME
from ANIMAL_INS AS INS
LEFT JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
order by INS.DATETIME