B
    a�*]k7  �            	   @   sD  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZm	Z	m
Z
 d dlmZ d dlmZ ejdd� ejdd�Zejd	d
d dd� e�� Zedd��Ze�� ZW dQ R X e�e�Zee
jej d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej d e
j ej  d e
j! d e
j ej d e
j ej  d e
j! d e
j ej d e
j ej  d e
j ej" d e
j ej  d e
j ej d  e
j ej d! e
j ej d" e
j ej  d e
j ej d# e
j! d$ e
j ej d% e
j! d& e
j ej d' e
j! d( e
j ej# d) e
j ej# d e
j ej# d* e
j ej d+ e
j ej# d e
j ej$ d, � e
jej Z%e
j!Z&e
jej  Z'e
jej Z(e
jej Z)e
jej Z*e
jej" Z+e
jej" Z,e
jej Z-e
jej. Z/e
jej# Z0e
jej# Z1e
jej$ Z2e �3� Z4d-Z5d.ed/ d0d1d2d3d4�Z6d5d6� Z7d7d8� Z8d9d:� Z9e4j:e5e6d;d<ed= d> ed= d? d@dA�dB�Z;e�e;j<�Z=y4ee%dC e' d e& e>e?e=dD dE �dF � � W n   edG� e�@�  Y nX e9eAe?edH �dF �eAe?edI �dF �� dS )J�    N)�Fore�Back�Style)�randint)�datetimeT)Z	autoresetz<999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk)Zdescriptionz-cz--betsetz%Enter Your Betset Number (default: 0))�default�helpzconfig.json�rz)
=======================================
uQ   🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲
z�      ___  _           ___       __
     / _ \(_)______   / _ )___  / /_
    / // / / __/ -_) / _  / _ \/ __/
   /____/_/\__/\__/ /____/\___/\__/u   🤖zV3.1.1 
uQ   
🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲z(
=======================================u   
🔘Author By  z: zKadal15
u   🔘Channel Yt �:z Jejaka Tutorialu   
🔘999 Dice Botz | zLose Streak �|z Win Streak
u8   🔘support by botakberambut(hijrah) & Termux_Id Member
u   🔘Donate z BTC z#18961sqv9fPuBcEbbi1gHub8ydWePB8yaG
z           LTC z#LNRkk6o9h1Rh98sDW8byeH9HbeUHwNohDu
z           Doge z$DJG4YG3ARUkSt9e5xvHvSS3faVx3v1HM9p

u   🔘Dev Sourcez Deri Sopiandi
u   🔘Channel Ytz	 X-XANADUz$https://www.999doge.com/api/web.aspxzfile://z
User-Agentz!application/x-www-form-urlencodedz*/*z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7zcom.reland.relandicebot)ZOriginz
user-agentzContent-typeZAcceptzAccept-LanguagezX-Requested-Withc             C   s�   t dt| � d �}|dks,|dks,|dkrbt |�d�d �}dt|� }tt|�d	|  �ada|d
ks�|dks�|dks�|dks�|dkr�dat|�d�d �ad S )Ni?B �d   �Hi�hiZHI�.�   �   �
   �LoZLOW�low�LowZLOr   )�str�float�split�len�intr   �high)ZpersenZtaruhan�c�nZpangkat� r   �
999dice.py�konvert8   s    (r    c             C   s�   t | �dk r4tdt | � �}|d t| � } d|  }t | �dkrjtdt | � �}|d t| � } d|  }n0t | �}| dd � }| d |d � }|d | }|S )N�   �0z0.i����r   )r   r   r   )ZnumZpanjang_nol�resultZlen_num�end�firstr   r   r   �revF   s    
r&   c       %      C   s�  t jdkst jdkst jdkrZd}d}x<|d7 }ytd | d }W q(   P Y q(X q(W n
tt j�}ttd | d �d	 }ttd | d
 �d }tttd | d �d �}ttd | d td | d d � |}dtd |ttt	dd�ddd�}	�y�t
jtt|	d�}
t�|
j�}|d t|d � t|� }t|d �t|� }t|d t|d � t|� | �d }ttd tttt|d �t|� �d � � ttd td | d  � d}d}d}d}t�� �d�}t|�ttd � }d}d}d}d}d}d}td | d }td | d }�
x�|dk�sH|dk�sH|d k�rNd}nd!}td | d" dk�s�td | d" d k�s�td | d" dk�r�tj�d#� n&|tttd | d" �d �k�r�|}td | d d$ d% d&k�s"td | d d$ d% d'k�s"td | d d$ d% d(k�r�|d7 }|d!k�r�|ttd | d d$ d) �d k�r^d*}|ttd | d d$ d) �d+ d k�r�d}d}|d!k�r|ttd | d d$ d, �d k�r�d*}|ttd | d d$ d, �d+ d k�rd}d}ntd | d d }t jdk�s0t jdk�s0t jdk�r�t�� �d�}t|�t|d �k�r�t|�ttd � }|d7 }||k�r~d}td-td | d  d. � ttd | d �d	 }ttd | d
 �d }tttd | d �d �}|}n
tt j�}td | d/ d% d'k�sDtd | d/ d% d&k�sDtd | d/ d% d(k�r tt�ttd | d/ d0 �ttd | d/ d1 ��d+�}tt|��}|d2k�r�tj�d3t|� d4 � |d5k�r�tj�d3t|� d6 � |d7k�r�tj�d3t|� d8 � t|t|�� nttd | d t|�� t �!t|�� t|�}|d7 }dtd |ttt	dd�ddd�}	|ttd9 �k�r�tt"d: t# d; t d< t t|� t$ d= t d> t% d? � t&�'d@t|� � t �!d� t&�'dAttt|d �t|� �d � � t�(�  t
jtt|	d�}
t�|
j�}t|d t|d � t|� | �d }t|d �t|� }|d | k�rtt)dB t t|� t) dC t* tt|�d � tttt|d �t|� �d � t*dD tt|� � ttdE � t&�'dF� t �!d� t&�'dAttt|d �t|� �d � � t�(�  |d |k �r�tt)dB t t|� t) dG t+ dH tt|�d � tttt|d �t|� �d � t+dI tt|� � tt,j-t.j/ dJ � t&�'dK� t �!d� t&�'dAttt|d �t|� �d � � t�(�  |d dk	�	r�|d7 }d}t|d �t|� } |dk�	rxtt)dB t t|� t) dC t* tt0t|��� ttt0t| ��� t*dD tt|� � nVtt)dB t t|� t) dC t* tt0t|��� ttt0t| ��� t+dI tt|� � t|�ttd | d) � }�nd}|d7 }d}!d!}t|d �t|� } |dk�
r|tt)dB t t|� t) dG t+ dH tt0t|��� ttt0t| ��� t*dD tt|� � nZtt)dB t t|� t) dG t+ dH tt0t|��� ttt0t| ��� t+dI tt|� � t|�ttd | d, � }|d!k�r|!d7 }!|!|k�rXd}!d}n@||k�rXd}|d!k�rT|t|�k�rX|}t|�t|� }n|}||k�rrd!}d}|d7 }||k�r�d!}d}|d7 }tj�tdL t t|� t% dM t t|� d3 � tdN d% d&k�s�tdN d% d'k�s�tdN d% d(k�r*tt0t| ���ttdN dO �k�r*dPtd tttdN dQ �d �tdN dR d#ddS�}"t
jtt|"d�}
t�|
j�}#td#� tdTtt0t|#dU ��� � t1dVdW��(}$|$�dTtt0t|#dU ��� dX � W d Q R X t�(�  �q*W W n�   td#� t&�'dY� y~t1dVdW��j}$|$�dBt�� �dZ� d[ t|� d\ t|� d] ttt|d �t|� �d � d^ t|� dX � W d Q R X W n   tt+d_ � Y nX t�(�  Y nX d S )`NZAuto�autoZAUTOr   r   ZConfigzName Bet SetZIntervali�  zReset If WinzBase Beti ��ZChanceZBetZPlaceBetZSessionCookiei?B Zdoge�2)�a�sZPayInr   ZHighZ
ClientSeed�CurrencyZProtocolVersion)�headers�dataZStartingBalanceZPayOutu   


🔥Starting Balanceu   🚀Anda Menggunakan BetSet Ke Fz%Mr   zReset If ProfitZOFFZOffZoffTzMax Bet� zHi / LowZToggleZOnZONZonzIf Winr   �   zIf LosezChange Bet Set z                           zRandom ChanceZMinZMax�   �z   �   z  �   � zTarget Profitz

Ok Boss Kuuh...! 
zProfit Mencapai Target.....!
zProfit z Doge
u-   
🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁u   
🔴DONE... !!!ztermux-toast You win ztermux-toast Total Balance �[z] ZProfitz)Yay.!
Balance Sudah Memenuhi Target.....!z&termux-toast Target Win Sudah Tercapai�]�-zLose zLose Target....!ztermux-toast Lose Target u         ✅Win Streak= u      ❎Lose Streak= zAuto Wdz
If BalanceZWithdraw�AmountzWallet Address)r)   r*   r8   ZAddress�Totpr+   z	Withdraw ZPendingzhistory.logza+�
ztermux-toast Betting Stopz%Y/%m/%d %H:%M:%Sz] Win Streak z Lose Streak z | Balance z Profit z%Balance Tidak Mencukupi Untuk Betting)2�my_namespaceZbetset�objr   r   r    �jsr   r   r   r   Zpost�url�ua�json�loads�text�print�hijau�resr   �birur   Znow�strftime�sys�stdout�write�round�randomZuniformr   �time�sleep�cyan�kuning�kuning2�red�os�system�exit�ungu�hijau2�red2r   �BRIGHTr   �REDr&   �open)%ZwsZlsZurutZjumlahulangZpesanZslpZlimit_aZpayinZamountr-   Zr1ZjsnZjumblZjumZprofr   ZburstZstats_rolebet_loseZstats_rolebet_winZmenitZno_winZno_loseZ	total_winZ
total_loseZ
no_rolebetZrolebetZreset_if_profitZtot_if_profitZstats_if_profitZwaktuZhasil_chanceZcokZbal�iZwdZwithdraw�fr   r   r   �diceX   sz   
&(.B"Z
&*
&*$

N:


@
*(f

*j

*
XV 
\Z





46"
,
rr^   ZLoginZ 7ec7f8a2c9724b2cbb8ed75e72b47ee9ZAccount�Username�Passwordr.   )r)   ZKeyr_   r`   r9   )r,   r-   u   
♦ ️Balance ZDogeZBalancei ��z%Check Your Username And Your Passwordz
Target WinzLose Target)BZrequestsr@   rM   rH   rL   rS   �argparseZcoloramar   r   r   r   r   Zinit�ArgumentParser�parser�add_argument�
parse_argsr;   r[   Zmyfile�readr-   rA   r<   rC   rY   ZMAGENTAZNORMALZCYANZGREENZDIMZWHITEZ	RESET_ALLrZ   ZYELLOWZBLACKrD   rE   Zabu2rV   Zungu2rW   rX   rR   rO   ZBLUErF   rP   rQ   ZabuZsessionr   r>   r?   r    r&   r^   �getr	   rB   r=   r   r   rU   r   r   r   r   r   �<module>   sb   8
� � Z,4