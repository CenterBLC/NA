# Data Feature Description


|feature|values|description|
|:-|:-|:-|
| orig_order | 1 2 3 ... 137777 137778 137779 | word order within corpus |
| bol_monad_num | 1 2 3 ... 137777 137778 137779 | BOL based word order within corpus |
| book_long | Matthew, Mark, Luke, John, Acts, Romans, I_Corinthians, II_Corinthians, Galatians, Ephesians, Philippians, Colossians, I_Thessalonians, II_Thessalonians, I_Timothy, II_Timothy, Titus, Philemon, Hebrews, James, I_Peter, II_Peter, I_John, II_John, III_John, Jude, Revelation | fully spelled out book name |
| booknum | 1 5 14 3 8 19 12 21 11 27 25 22 26 15 9 6 13 23 4 16 20 10 2 17 18 24 | NT book number (Matthew=1, Mark=2, Revelation=27 |
| book_short | Matt, Mark, Luke, John, Acts, Rom, 1Cor, 2Cor, Gal, Eph, Phil, Col, 1Thess, 2Thess, 1Tim, 2Tim, Titus, Phlm, Heb, Jas, 1Pet, 2Pet, 1John, 2John, 3John, Jude, Rev | book name abbreviated |
| chapter | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 2 25 26 27 28 | chapter number |
| verse | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 2 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 4 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 7 73 74 75 99 76 77 78 79 80 | verse number |
| bol_ref | Matt 1:1, Matt 1:2, Matt 1:3, ... ,Rev 22:19, Rev 22:20, Rev 22:21 | BOL based Bible reference |
| word | Βίβλος, γενέσεως, Ἰησοῦ, ... ,ἀφέλῃ, ἀφελεῖ, ἁγίας | word as it appears in the text |
| bol_surface | Βίβλος, γενέσεως, Ἰησοῦ, ... ,ἀφέλῃ, ἀφελεῖ, ἁγίας | BOL based word as it appears in the text |
| normalized | Βίβλος, γενέσεως, Ἰησοῦ, ... ,γεγραμμένας, ἀφέλῃ, ἀφελεῖ | normalized word |
| lemma | βίβλος, γένεσις, Ἰησοῦς, ... ,διαυγής, κατάθεμα, ῥυπαίνω | lexeme |
| bol_lemma | βίβλος, γένεσις, Ἰησοῦς, ... ,διαυγής, κατάθεμα, ῥυπαίνω | BOL based lexeme |
| lemma_translit | biblos, genesis, Iesous, ... ,diauges, katathema, Rupaino | lexeme tranliterated |
| form_tag | N-NSF, N-GSF, N-GSM, ... ,V-IAI-1S-ATT, V-2RAP-NSN, A-APF-S | form tag |
| functional_tag | N-NSF, N-GSF, N-GSM, ... ,V-IAI-1S-ATT, A-APF-S, V-RMP-NPM | functional tag |
| strongs | 976 1078 2424 ... 271 2652 4510 | strongs number |
| strongs_unreliable | False True | unreliable strongs number |
| lexeme_dict | βίβλος,\xa0-ου,\xa0ἡ, γένεσις,\xa0-εως,\xa0ἡ, Ἰησοῦς, ... ,διαυγής,\xa0-ές, κατάθεμα,\xa0-τος,\xa0τό, ῥυπαίνομαι | lexema as it appears in the dictionary |
| bol_lemma_dict | βίβλος,\xa0-ου,\xa0ἡ, γένεσις,\xa0-εως,\xa0ἡ, Ἰησοῦς, ... ,διαυγής,\xa0-ές, κατάθεμα,\xa0-τος,\xa0τό, ῥυπαίνομαι | lexema as it appears in the BOL dictionary |
| gloss | written book, roll, or volume, birth, lineage, Jesus, ..., amethyst, curse, accursed thing, am filthy | English gloss |
| bol_gloss | written book, roll, or volume, birth, lineage, Jesus, ..., amethyst, curse, accursed thing, am filthy | BOL based English gloss |
| abc_order | 965 1067 2387 ... 1291 2576 4320 | the dictionary position of a given word |
| bol_dict_abc | 969 1070 2399 ... 1295 2590 4347 | BOL based the dictionary position of a given word |
| freq_lemma | 10 5 913 529 376 59 73 97 19783 20 2787 2 44 8978 343 5550 3 1 2 115 12 886 4 47 35 216 54 1407 2255 1242 496 43 647 147 209 245 84 13 30 176 2743 9 709 379 234 79 1060 20 37 66 1388 682 718 472 6 31 95 49 214 289 1038 18 148 229 106 142 173 108 668 669 86 9 219 667 144 15 8 2567 1311 143 566 502 7 162 221 389 11 1766 139 45 194 24 635 60 428 12 63 192 250 14 217 28 145 68 159 153 333 5 46 53 19 74 243 94 90 78 17 700 154 10 29 25 164 110 117 61 1293 131 413 40 99 10 102 21 22 412 42 163 244 134 47 34 162 27 41 16 33 76 98 562 36 62 331 71 180 23 91 87 81 82 23 39 501 114 140 548 638 6 93 141 185 166 414 337 119 72 120 133 75 15 56 174 261 50 26 123 235 48 169 126 336 15 100 258 70 32 150 320 158 57 118 135 80 24 128 38 55 112 113 298 92 58 69 51 124 7 88 179 116 65 | number of occurence of a given lexeme |
| bol_lexeme_occurrences | 10 5 913 529 376 59 73 97 19783 20 2787 2 37 8978 343 5550 3 1 2 115 12 886 4 47 35 216 54 1407 2255 1242 496 43 647 147 209 245 84 13 30 176 2743 9 709 379 234 79 1060 20 66 1388 682 718 472 6 31 95 49 214 2892 103 18 148 229 106 142 173 108 668 669 86 96 21 667 144 15 8 2567 1311 143 566 502 7 1622 22 44 389 11 1766 63 45 194 24 635 60 428 12 192 250 217 28 140 68 159 153 333 52 46 5 19 74 243 94 90 78 17 700 154 101 14 2 25 164 110 117 61 1293 132 139 354 40 99 10 102 21 22 412 42 163 244 134 47 34 162 27 41 16 33 76 98 562 36 62 320 71 180 23 91 87 81 82 23 39 501 548 638 67 93 14 185 166 414 337 119 72 120 133 75 156 56 17 261 50 26 123 235 48 169 126 336 55 58 10 331 114 258 70 32 150 57 118 135 80 241 12 38 112 113 65 298 92 69 51 124 77 88 17 116 155 158 | BOL based number of occurence of a given lexeme |
| bol_frequency_rank | 1052 1638 19 35 47 275 232 170 1 620 5 500 395 49 3 2180 3490 2656 143 902 21 1864 41 415 73 294 1 9 16 39 348 29 109 75 8 201 863 461 87 6 113 23 46 67 212 17 78 250 13 25 22 40 1469 444 17 314 74 4 18 659 107 69 155 115 91 153 27 26 19 176 71 28 111 764 1237 7 14 112 32 37 1347 11 7 343 45 968 10 256 337 79 545 31 270 42 133 81 6 72 484 118 241 98 104 53 303 329 298 641 230 63 18 191 217 697 24 103 161 811 470 531 94 149 140 265 1 126 121 48 376 167 151 157 603 582 44 354 95 62 12 322 422 96 58 363 726 432 222 169 33 404 261 55 23 85 68 187 196 208 205 563 384 38 34 30 244 183 11 84 93 43 51 136 234 135 124 227 100 286 90 59 30 514 132 66 319 92 129 52 291 281 165 54 144 60 23 438 106 283 138 122 211 65 127 390 148 147 254 57 18 240 307 131 220 195 86 142 102 99 | BOL based frequency rank of a given lexeme |
| sp | noun, verb, art, conj, prep, pron-rela, adj, adv, interj, pron-reflex, hebrew, aramaic, pron-indefi, pron-correl-interrog, pron-posses, pron-correl | part of speech |
| bol_psp | noun, verb, art, conj, prep, pron-rela, adj, adv, interj, pron-reflex, hebrew, aramaic, pron-indefi, pron-correl-interrog, pron-posses, pron-correl | BOL based part of speech |
| gn | f, m, n, nan | gender |
| bol_gender | feminine, masculine, neuter, nan | BOL based gender |
| nu | sg, pl, nan | number |
| bol_number | singular, plural, nan | BOL based number |
| nu_poss | sg, pl, nan | number of posessor |
| bol_possessor_number | singular, plural, nan | BOL based number of posessor |
| ps | p1, p2, p3, nan | person |
| bol_person | first_person, second_person, third_person, nan | BOL based person |
| case | nom, gen, dat, acc, voc, nan | case |
| bol_case | nominative, genitive, dative, accusative, vocative, nan | BOL based case |
| tense | aorist, present, imperfect, second_aorist, future, second_perfect, perfect, second_future, pluperfect, second_pluperfect, nan | tense |
| bol_tense | aorist, present, imperfect, second_aorist, future, second_perfect, perfect, second_future, pluperfect, second_pluperfect, nan | BOL based tense |
| voice | a, p, m_or_p, pd, m, md, m_or_pd, nan | voice |
| bol_voice | active, passive, middle_or_passive, passive_deponent, middle, middle_deponent, middle_or_passive_deponent, nan | BOL based voice |
| mood | ind, ptc, inf, imp, sbj, opt, nan | mood |
| bol_mood | indicative, participle, infinitive, imperative, subjunctive, optative, nan | BOL based mood |
| degree | superlative, comparative, nan | degree |
| extra | negative, interrogative, superlative, crasis, comparative, attic, particle_attached, nan | extra |
| bol_suffix | negative, interrogative, superlative, crasis, comparative, attic, particle_attached, nan | BOL based suffix |
| bol_verb_type | alpha, gamma, irregular, epsilon_upsilon, khi, sigma_kappa, lambda, zeta, upsilon, epsilon, nu, tau, omicron, rho, kappa, phi, pi, mu_iota, iota, eta, delta, theta, beta, mu, nan | BOL based verb type |
| bol_noun_stem | omicron, iota, irregular, alpha, epsilon_upsilon, nu, rho, tau, delta, sigma, khi, upsilon, nu_tau, kappa, indeclinable, pi, gamma, omicron_upsilon, beta, kappa_tau, omega, nan | BOL based noun type/noun stem |
| word_stem | iota, irregular, alpha, epsilon_upsilon, gamma, khi, lambda, epsilon, kappa, mu_iota, delta, eta, beta, indeclinable, mu, kappa_tau, nan | stem of word |
| declension | 2nd, 3rd, irregular, 1st_alpha_macron_doric, 1st_alpha_macron, 1st_eta, 1st_alpha_breve, indeclinable, 2nd_attic, nan | noun declension |
| bol_noun_declension | second_d, third_d, irregular, first_alpha_macron_doric, first_alpha_macron, first_eta, first_alpha_breve, indeclinable, second_attic, nan | BOL based noun declension |
| vocab_ReadGreekIn30Days | 3a, 3b, 4a, 4b, … | chapter categoried vocab as it appears in Larry Richards Textbook "Learning Greek in 30 days |
