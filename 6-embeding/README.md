# Embedding

- **Embedding**은 **Vector**라고 하는 일련의 숫자로 텍스트의 의미를 포착 후, 해당 벡터를 사용해 **텍스트가 서로 얼마나 유사한지 확인**
- **Vector Database**를 사용해 Embedding을 저장하고 빠른 유사도 검색을 수행할 수 있음
- **Vector Database**와 결합된 임베딩은 **검색 증강 생성(RAG)**의 핵심 구성 요소임

> 해당 실습에서는 Python에 내장된 math.dist() 함수를 사용해 유사성을 판단합니다.  
> 실제 애플리케이션에서는 코사인 유사도(cosine similarity) 및 도트 곱(dot product) 계산을 포함하여 벡터 데이터베이스가 임베딩을 비교하는 데 사용하는 다른 방법도 있습니다.

## 테스트

```zsh
❯ python3 bedrock_embedding.py
Closest matches for 'Felines, canines, and rodents'
----------------
1.000000         Felines, canines, and rodents
0.872856         Cats, dogs, and mice
0.599730         Chats, chiens et souris
0.516598         Lions, tigers, and bears
0.456268         고양이, 개, 쥐
0.455923         猫、犬、ネズミ
0.068916         パン屋への道順を知りたい
0.061314         パン屋への行き方を教えてください
0.034925         빵집으로 가는 길을 알려주세요.
0.024160         경기장 가는 방법을 알려주시겠어요?
0.002239         Can you please tell me how to get to the stadium?
-0.003159        Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
-0.007595        Can you please tell me how to get to the bakery?
-0.019469        Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
-0.020840        I need directions to the bread shop

Closest matches for 'Can you please tell me how to get to the bakery?'
----------------
1.000000         Can you please tell me how to get to the bakery?
0.712236         I need directions to the bread shop
0.541959         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.492384         빵집으로 가는 길을 알려주세요.
0.484672         Can you please tell me how to get to the stadium?
0.455479         パン屋への行き方を教えてください
0.406388         パン屋への道順を知りたい
0.369163         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.238000         경기장 가는 방법을 알려주시겠어요?
0.109972         고양이, 개, 쥐
0.078357         猫、犬、ネズミ
0.022138         Cats, dogs, and mice
0.015661         Lions, tigers, and bears
0.005211         Chats, chiens et souris
-0.007595        Felines, canines, and rodents

Closest matches for 'Lions, tigers, and bears'
----------------
1.000000         Lions, tigers, and bears
0.530917         Cats, dogs, and mice
0.516598         Felines, canines, and rodents
0.386125         Chats, chiens et souris
0.337012         猫、犬、ネズミ
0.329288         고양이, 개, 쥐
0.068164         I need directions to the bread shop
0.056721         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.054695         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.045133         경기장 가는 방법을 알려주시겠어요?
0.042972         パン屋への道順を知りたい
0.032731         Can you please tell me how to get to the stadium?
0.031754         빵집으로 가는 길을 알려주세요.
0.021517         パン屋への行き方を教えてください
0.015661         Can you please tell me how to get to the bakery?

Closest matches for 'Chats, chiens et souris'
----------------
1.000000         Chats, chiens et souris
0.669460         Cats, dogs, and mice
0.599730         Felines, canines, and rodents
0.503684         고양이, 개, 쥐
0.498394         猫、犬、ネズミ
0.386125         Lions, tigers, and bears
0.299799         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.156950         パン屋への道順を知りたい
0.131597         パン屋への行き方を教えてください
0.091534         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.086036         빵집으로 가는 길을 알려주세요.
0.025773         I need directions to the bread shop
0.005211         Can you please tell me how to get to the bakery?
-0.000786        경기장 가는 방법을 알려주시겠어요?
-0.036810        Can you please tell me how to get to the stadium?

Closest matches for '猫、犬、ネズミ'
----------------
1.000000         猫、犬、ネズミ
0.759887         고양이, 개, 쥐
0.503620         Cats, dogs, and mice
0.498394         Chats, chiens et souris
0.487732         パン屋への道順を知りたい
0.460217         パン屋への行き方を教えてください
0.455923         Felines, canines, and rodents
0.350541         빵집으로 가는 길을 알려주세요.
0.337012         Lions, tigers, and bears
0.203162         경기장 가는 방법을 알려주시겠어요?
0.162600         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.153400         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.078357         Can you please tell me how to get to the bakery?
0.063395         I need directions to the bread shop
0.014240         Can you please tell me how to get to the stadium?

Closest matches for 'Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?'
----------------
1.000000         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.592948         I need directions to the bread shop
0.541959         Can you please tell me how to get to the bakery?
0.530933         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.508951         빵집으로 가는 길을 알려주세요.
0.433526         パン屋への行き方を教えてください
0.383732         パン屋への道順を知りたい
0.299799         Chats, chiens et souris
0.241092         Can you please tell me how to get to the stadium?
0.238161         고양이, 개, 쥐
0.187804         경기장 가는 방법을 알려주시겠어요?
0.153400         猫、犬、ネズミ
0.056721         Lions, tigers, and bears
0.031843         Cats, dogs, and mice
-0.019469        Felines, canines, and rodents

Closest matches for 'Kannst du mir bitte sagen, wie ich zur Bäckerei komme?'
----------------
1.000000         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.530933         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.431125         빵집으로 가는 길을 알려주세요.
0.419582         I need directions to the bread shop
0.369163         Can you please tell me how to get to the bakery?
0.360738         パン屋への行き方を教えてください
0.307116         パン屋への道順を知りたい
0.270668         Can you please tell me how to get to the stadium?
0.270667         경기장 가는 방법을 알려주시겠어요?
0.199114         고양이, 개, 쥐
0.162600         猫、犬、ネズミ
0.091534         Chats, chiens et souris
0.054695         Lions, tigers, and bears
0.028943         Cats, dogs, and mice
-0.003159        Felines, canines, and rodents

Closest matches for 'パン屋への行き方を教えてください'
----------------
1.000000         パン屋への行き方を教えてください
0.895563         パン屋への道順を知りたい
0.607981         빵집으로 가는 길을 알려주세요.
0.491218         I need directions to the bread shop
0.460217         猫、犬、ネズミ
0.455479         Can you please tell me how to get to the bakery?
0.433526         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.367932         고양이, 개, 쥐
0.360738         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.321858         경기장 가는 방법을 알려주시겠어요?
0.220985         Can you please tell me how to get to the stadium?
0.131597         Chats, chiens et souris
0.078212         Cats, dogs, and mice
0.061314         Felines, canines, and rodents
0.021517         Lions, tigers, and bears

Closest matches for 'パン屋への道順を知りたい'
----------------
1.000000         パン屋への道順を知りたい
0.895563         パン屋への行き方を教えてください
0.607788         빵집으로 가는 길을 알려주세요.
0.487732         猫、犬、ネズミ
0.466405         I need directions to the bread shop
0.433397         고양이, 개, 쥐
0.406388         Can you please tell me how to get to the bakery?
0.383732         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.311356         경기장 가는 방법을 알려주시겠어요?
0.307116         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.156950         Chats, chiens et souris
0.131994         Can you please tell me how to get to the stadium?
0.101027         Cats, dogs, and mice
0.068916         Felines, canines, and rodents
0.042972         Lions, tigers, and bears

Closest matches for 'Can you please tell me how to get to the stadium?'
----------------
1.000000         Can you please tell me how to get to the stadium?
0.484672         Can you please tell me how to get to the bakery?
0.450129         경기장 가는 방법을 알려주시겠어요?
0.305550         I need directions to the bread shop
0.270668         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.259428         빵집으로 가는 길을 알려주세요.
0.241092         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.220985         パン屋への行き方を教えてください
0.131994         パン屋への道順を知りたい
0.032731         Lions, tigers, and bears
0.014240         猫、犬、ネズミ
0.012097         고양이, 개, 쥐
0.002239         Felines, canines, and rodents
-0.008508        Cats, dogs, and mice
-0.036810        Chats, chiens et souris

Closest matches for 'I need directions to the bread shop'
----------------
1.000000         I need directions to the bread shop
0.712236         Can you please tell me how to get to the bakery?
0.592948         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.542894         빵집으로 가는 길을 알려주세요.
0.491218         パン屋への行き方を教えてください
0.466405         パン屋への道順を知りたい
0.419582         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.305550         Can you please tell me how to get to the stadium?
0.191226         경기장 가는 방법을 알려주시겠어요?
0.126749         고양이, 개, 쥐
0.068164         Lions, tigers, and bears
0.063395         猫、犬、ネズミ
0.025934         Cats, dogs, and mice
0.025773         Chats, chiens et souris
-0.020840        Felines, canines, and rodents

Closest matches for 'Cats, dogs, and mice'
----------------
1.000000         Cats, dogs, and mice
0.872856         Felines, canines, and rodents
0.669460         Chats, chiens et souris
0.530917         Lions, tigers, and bears
0.503620         猫、犬、ネズミ
0.498377         고양이, 개, 쥐
0.101027         パン屋への道順を知りたい
0.078212         パン屋への行き方を教えてください
0.068564         빵집으로 가는 길을 알려주세요.
0.031843         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.028943         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.025934         I need directions to the bread shop
0.022138         Can you please tell me how to get to the bakery?
0.016569         경기장 가는 방법을 알려주시겠어요?
-0.008508        Can you please tell me how to get to the stadium?

Closest matches for '고양이, 개, 쥐'
----------------
1.000000         고양이, 개, 쥐
0.759887         猫、犬、ネズミ
0.503684         Chats, chiens et souris
0.498377         Cats, dogs, and mice
0.482159         빵집으로 가는 길을 알려주세요.
0.456268         Felines, canines, and rodents
0.433397         パン屋への道順を知りたい
0.367932         パン屋への行き方を教えてください
0.334550         경기장 가는 방법을 알려주시겠어요?
0.329288         Lions, tigers, and bears
0.238161         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.199114         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.126749         I need directions to the bread shop
0.109972         Can you please tell me how to get to the bakery?
0.012097         Can you please tell me how to get to the stadium?

Closest matches for '경기장 가는 방법을 알려주시겠어요?'
----------------
1.000000         경기장 가는 방법을 알려주시겠어요?
0.613277         빵집으로 가는 길을 알려주세요.
0.450129         Can you please tell me how to get to the stadium?
0.334550         고양이, 개, 쥐
0.321858         パン屋への行き方を教えてください
0.311356         パン屋への道順を知りたい
0.270667         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.238000         Can you please tell me how to get to the bakery?
0.203162         猫、犬、ネズミ
0.191226         I need directions to the bread shop
0.187804         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.045133         Lions, tigers, and bears
0.024160         Felines, canines, and rodents
0.016569         Cats, dogs, and mice
-0.000786        Chats, chiens et souris

Closest matches for '빵집으로 가는 길을 알려주세요.'
----------------
1.000000         빵집으로 가는 길을 알려주세요.
0.613277         경기장 가는 방법을 알려주시겠어요?
0.607981         パン屋への行き方を教えてください
0.607788         パン屋への道順を知りたい
0.542894         I need directions to the bread shop
0.508951         Pouvez-vous s'il vous plaît me dire comment me rendre à la boulangerie?
0.492384         Can you please tell me how to get to the bakery?
0.482159         고양이, 개, 쥐
0.431125         Kannst du mir bitte sagen, wie ich zur Bäckerei komme?
0.350541         猫、犬、ネズミ
0.259428         Can you please tell me how to get to the stadium?
0.086036         Chats, chiens et souris
0.068564         Cats, dogs, and mice
0.034925         Felines, canines, and rodents
0.031754         Lions, tigers, and bears
```
