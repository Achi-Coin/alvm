IF_COST = 33
CONS_COST = 50
FIRST_COST = 30
REST_COST = 30
LISTP_COST = 19

MALLOC_COST_PER_BYTE = 10

ARITH_BASE_COST = 99
ARITH_COST_PER_BYTE = 3
ARITH_COST_PER_ARG = 320

LOG_BASE_COST = 100
LOG_COST_PER_BYTE = 3
LOG_COST_PER_ARG = 264

GRS_BASE_COST = 117
GRS_COST_PER_BYTE = 1

EQ_BASE_COST = 117
EQ_COST_PER_BYTE = 1

GR_BASE_COST = 498
GR_COST_PER_BYTE = 2

DIVMOD_BASE_COST = 1116
DIVMOD_COST_PER_BYTE = 6

DIV_BASE_COST = 988
DIV_COST_PER_BYTE = 4

SHA256_BASE_COST = 87
SHA256_COST_PER_ARG = 134
SHA256_COST_PER_BYTE = 2

POINT_ADD_BASE_COST = 101094
POINT_ADD_COST_PER_ARG = 1343980

PUBKEY_BASE_COST = 1325730
PUBKEY_COST_PER_BYTE = 38

MUL_BASE_COST = 92
MUL_COST_PER_OP = 885
MUL_LINEAR_COST_PER_BYTE = 6
MUL_SQUARE_COST_PER_BYTE_DIVIDER = 128

STRLEN_BASE_COST = 173
STRLEN_COST_PER_BYTE = 1

PATH_LOOKUP_BASE_COST = 40
PATH_LOOKUP_COST_PER_LEG = 4
PATH_LOOKUP_COST_PER_ZERO_BYTE = 4

CONCAT_BASE_COST = 142
CONCAT_COST_PER_ARG = 135
CONCAT_COST_PER_BYTE = 3

BOOL_BASE_COST = 200
BOOL_COST_PER_ARG = 300

ASHIFT_BASE_COST = 596
ASHIFT_COST_PER_BYTE = 3

LSHIFT_BASE_COST = 277
LSHIFT_COST_PER_BYTE = 3

LOGNOT_BASE_COST = 331
LOGNOT_COST_PER_BYTE = 3

APPLY_COST = 90
QUOTE_COST = 20