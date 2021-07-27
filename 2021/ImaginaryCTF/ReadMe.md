# Challenges

## Chicken Caesar Salad

#### Description
[chicken_caesor_salad](./photos/chicken.png)
- We are provided with a text file with the cipher text:
```
qkbn{ePmv_lQL_kIMamZ_kQxpMZa_oMb_aW_pIZl}
```
#### Solution
Points to note:
- caesar cipher is a substitution cipher
Identify the shift value:
- we know the flag format is **ictf**{...} and has been shifted ti **qkbn**{...}
- from **i** to **q** there is a shift value of +8
To obtain the flag, do a -18 shift on the cipher text
- A simple script to solve: [chicken_caesor_salad](./chicken_caesor_salad.py) gets us the flag
```
ictf{wHen_dID_cAEseR_cIphERs_gEt_sO_hARd}

```

## Hidden

#### Description
[Hidden](./hidden.png)

#### Solution
- checking file with exiftool reveals its a photoshop file, but i only have linux
- Tried opening with gimp but got an error
- Decided to check the string and got:
```
ictf{wut_how_do_you_see_this}

```

## roos_world

#### Description
[roos_World](./photos/roo.png)
- Roo be looking for the flag<br>
He might need to get a magnifying glass to inspect this website better

#### solution
- clue from the descrption is inspect. From the source code we get:
```
<!--You know Roo, its not THAT easy to get the flag. Go think some more-->
``` 
- Checked robots.txt, received 404 not found
- Hmmm, decided to inspect the console output:
[roos_flag](./photos/roo_flag.png)
- Found our flag:
```
ictf{1nsp3ct0r_r00_g0es_th0nk}
```
