"""
Supreme Court prediction model data
@date 20150926
@author mjbommar
"""

# Court to circuit mapping, which maps from SCDB codebook to the actual Circuit number
# http://scdb.wustl.edu/documentation.php?var=caseOrigin
# http://scdb.wustl.edu/documentation.php?var=caseSource
court_circuit_map = {1: 13,
                     2: 13, 3: 13, 4: 14, 5: 14, 6: 13, 7: 13, 8: 13,
                     9: 22, 10: 99, 12: 9, 13: 99, 14: 13, 15: 99, 16: 99,
                     17: 99, 18: 99, 19: 0, 20: 22, 21: 1, 22: 2, 23: 3,
                     24: 4, 25: 5, 26: 6, 27: 7, 28: 8, 29: 9, 30: 10,
                     31: 11, 32: 12, 41: 11, 42: 11, 43: 11, 44: 9, 45: 9,
                     46: 8, 47: 8, 48: 9, 49: 9, 50: 9, 51: 9, 52: 10, 53: 2,
                     54: 3, 55: 12, 56: 11, 57: 11, 58: 11, 59: 11, 60: 11,
                     61: 11, 62: 9, 63: 9, 64: 9, 65: 7, 66: 7, 67: 7, 68: 7,
                     69: 7, 70: 8, 71: 8, 72: 10, 73: 6, 74: 6, 75: 5, 76: 5,
                     77: 5, 78: 1, 79: 4, 80: 1, 81: 6, 82: 6, 83: 8, 84: 5,
                     85: 5, 86: 8, 87: 8, 88: 9, 89: 8, 90: 9, 91: 1, 92: 3,
                     93: 10, 94: 2, 95: 2, 96: 2, 97: 2, 98: 4, 99: 4, 100: 4,
                     101: 8, 102: 9, 103: 6, 104: 6, 105: 10, 106: 10, 107: 10,
                     108: 9, 109: 3, 110: 3, 111: 3, 112: 1, 113: 1, 114: 4,
                     115: 8, 116: 6, 117: 6, 118: 6, 119: 5, 120: 5, 121: 5,
                     122: 5, 123: 10, 124: 2, 125: 3, 126: 4, 127: 4, 128: 9,
                     129: 9, 130: 4, 131: 4, 132: 7, 133: 7, 134: 10, 150: 5,
                     151: 9, 152: 4, 153: 7, 155: 4, 160: 4, 162: 11, 163: 5,
                     164: 11, 165: 7, 166: 7, 167: 8, 168: 6, 169: 5, 170: 8,
                     171: 3, 172: 3, 173: 2, 174: 4, 175: 6, 176: 3, 177: 3,
                     178: 5, 179: 4, 180: 4, 181: 7, 182: 6, 183: 3, 184: 9,
                     185: 11, 186: 8, 187: 5, 300: 0, 301: 0, 302: 0, 400: 99,
                     401: 99, 402: 99, 403: 11, 404: 8, 405: 9, 406: 2, 407: 3,
                     408: 11, 409: 11, 410: 7, 411: 7, 412: 8, 413: 10, 414: 6,
                     415: 5, 416: 1, 417: 4, 418: 1, 419: 6, 420: 8,
                     421: 5, 422: 8, 423: 9, 424: 1, 425: 3, 426: 2,
                     427: 4, 428: 6, 429: 9, 430: 3, 431: 1, 432: 4, 433: 6,
                     434: 5, 435: 2, 436: 4, 437: 4, 438: 7,
                     439: 10, 440: 12, 441: 8, 442: 10, 443: 9}

# Party mapping
party_map_data = {1:2, 2:5, 3:4, 4:5, 5:4, 6:13, 7:0, 8:11, 9:11, 10:11, 11:11,
    12:0, 13:11, 14:0, 15:0, 16:13, 17:0, 18:4, 19:0, 20:13, 21:4, 22:0, 23:0, 24:0,
    25:8, 26:0, 27:2, 28:5, 100:3, 101:1, 102:0, 103:1, 104:1, 105:1, 106:9, 107:0,
    108:0, 109:1, 110:3, 111:0, 112:0, 113:1, 114:0, 115:1, 116:1, 117:1, 118:1,
    119:1, 120:1, 121:1, 122:1, 123:1, 124:1, 125:1, 126:3, 127:0, 128:1, 129:0,
    130:0, 131:0, 132:1, 133:1, 134:14, 135:0, 136:0, 137:3, 138:0, 139:1, 140:0,
    141:1, 142:0, 143:1, 144:1, 145:11, 146:0, 147:1, 148:1, 149:0, 150:14, 151:0,
    152:1, 153:0, 154:11, 155:0, 156:0, 157:1, 158:1, 159:0, 160:1, 161:1, 162:0,
    163:0, 164:0, 165:1, 166:0, 167:1, 168:0, 169:0, 170:6, 171:1, 172:0, 173:0,
    174:0, 175:0, 176:0, 177:0, 178:1, 179:0, 180:0, 181:1, 182:11, 183:11, 184:1,
    185:1, 186:0, 187:1, 188:0, 189:1, 190:1, 191:1, 192:1, 193:9, 194:1, 195:0,
    196:0, 197:0, 198:1, 199:0, 200:3, 201:0, 202:0, 203:0, 204:0, 205:1, 206:0,
    207:14, 208:0, 209:1, 210:0, 211:0, 212:0, 213:3, 214:0, 215:3, 216:0, 217:3,
    218:14, 219:1, 220:1, 221:0, 222:0, 223:14, 224:0, 225:0, 226:0, 227:0, 228:1,
    229:0, 230:0, 231:1, 232:0, 233:1, 234:1, 235:1, 236:0, 237:0, 238:1, 239:0,
    240:8, 241:0, 242:0, 243:1, 244:0, 245:1, 246:1, 247:12, 248:0, 249:12, 250:0,
    251:0, 252:0, 253:0, 254:0, 255:0, 256:0, 257:0, 258:2, 259:1, 301:2, 302:2,
    303:2, 304:2, 305:2, 306:2, 307:2, 308:2, 309:2, 310:2, 311:2, 312:2, 313:2,
    314:2, 315:2, 316:2, 317:2, 318:2, 319:2, 320:2, 321:2, 322:2, 323:2, 324:2,
    325:2, 326:2, 327:2, 328:2, 329:2, 330:2, 331:2, 332:2, 333:2, 334:2, 335:2,
    336:2, 337:2, 338:2, 339:2, 340:2, 341:2, 342:2, 343:2, 344:2, 345:2, 346:2,
    347:2, 348:2, 349:2, 350:2, 351:2, 352:2, 353:2, 354:2, 355:2, 356:2, 357:2,
    358:2, 359:2, 360:2, 361:2, 362:2, 363:2, 364:2, 366:2, 367:2, 368:2, 369:2,
    370:2, 371:2, 372:2, 373:2, 374:2, 375:2, 376:2, 377:2, 378:2, 379:2, 380:2,
    381:2, 382:2, 383:2, 384:2, 385:2, 386:2, 387:2, 388:2, 389:2, 390:2, 391:2,
    392:2, 393:2, 394:2, 395:2, 396:2, 397:2, 398:2, 399:2, 400:2, 401:2, 402:2,
    403:2, 404:2, 405:2, 406:2, 407:2, 408:2, 409:2, 410:2, 411:2, 412:2, 413:2,
    414:2, 415:2, 416:2, 417:2, 501:0, 600:0,}


