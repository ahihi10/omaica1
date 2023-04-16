

from production import IF, AND, THEN, FAIL, OR

RULES = (
    
    IF("(?x) is a businessman",
        THEN("(?x) makes millions")),
    IF("(?x) is in the mob",
        THEN("(?x) has low taxes")),
    IF(AND("(?x) has low taxes", "(?x) makes millions"), 
        THEN("(?x) embezzles money")),
    IF("(?x) embezzles money", 
        THEN("(?x) is a criminal")),
    IF(AND("(?x) knows (?y)", "(?x) makes millions", "(?y) is in the mob"),
        THEN(AND("(?x) has low taxes", "(?x) gets out of jail")))
)
   
DATA = (
    "Gotti is in the mob", "Cagoni is a businessman", "Cagoni knows Gotti"
)
