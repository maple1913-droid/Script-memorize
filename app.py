import streamlit as st

# 페이지 설정 (모바일 최적화)
st.set_page_config(page_title="뮤지컬 <썸데이> 지해 대본 연습", page_icon="🎭", layout="centered")

# 전체 대본 데이터베이스 (지해 대사 큐 및 다음 상대방 대사)
SCENES = {
    "1. 오디션 및 첫 등장": [
        {
            "cue": "안녕하세요, 오디션 번호 000번 000입니다! (하고 싶은 말, 포부 등)",
            "speaker": "지해",
            "next_speaker": "썸데이",
            "next_line": "안녕하세요, 오디션 번호 000번 000입니다! (하고 싶은 말, 포부 등) 감사합니다!"
        }
    ],
    "2. 첫 번째 바(Bar) 방문": [
        {
            "cue": "지금을 기억할게, 순간이 모여 처음이 된 그 어느 날.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "저기 혹시, 그 술 이름이 뭐예요?"
        },
        {
            "cue": "무슨 일이 있어야 마시나요... 그냥 일상적으로다가...",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "아, 그래요?"
        },
        {
            "cue": "오늘이 대학교 합격자 발표 날이거든요.",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "오! 분위기가 떨어진 분위기가 아닌데? 축하드립니다. 한 잔 더 드릴까요?"
        },
        {
            "cue": "네. 제가 사실 글 쓰는 걸 좋아하는데... 대학에 막상 덜컥 붙어 버리니까 걱정이 되네요.",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "우와, 작가이신 거예요?"
        },
        {
            "cue": "지망생인 거죠.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "저랑 같네요!"
        },
        {
            "cue": "아니 저도 글을 쓰긴 하는데 글은 가사 쪽만 하고... 일단은 작곡을 좀 더...",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "와 멋있다."
        },
        {
            "cue": "오늘 달달하고 기분 좋은 맛은 느껴야 할 것 같지만, 또 취하긴 해야 할 것 같아서요.",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "딱 좋은데요?"
        }
    ],
    "3. 두 번째 바 방문 (이암과의 만남)": [
        {
            "cue": "계세요~?",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "어서 오세요."
        },
        {
            "cue": "혹시... 여기서 노래도 하나요?",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "네?"
        },
        {
            "cue": "아니에요.",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "그... 병원 이야기 좀 해주세요. 뭐가 좀 안 좋은 데가 있으셨던 거예요?"
        },
        {
            "cue": "아, 기억 하시네...",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "어제 들었습니다."
        },
        {
            "cue": "네...?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "네."
        },
        {
            "cue": "저 이만 가볼게요.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "많이 남았는데."
        },
        {
            "cue": "아, 너무 맛있다.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "급한 일 있으세요?"
        },
        {
            "cue": "제가 술을 좋아해요.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "네?"
        },
        {
            "cue": "아, 완샷이 원래 일상생활이니까 이상하게 생각하지 마시라 뭐 그런 거죠.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "저기 혹시 실례가 안 된다면, 이야기 좀 더 나눌 수 있을까요?"
        },
        {
            "cue": "네 잘 알죠! 아뇨, 아 그랬군요, 축하드려요....",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "실은 제가 노래를 하는데요."
        }
    ],
    "4. 연수와의 대화 및 꿈 이야기": [
        {
            "cue": "내가 특별히 관심은 없어서 잘은 모르는데, 여기 사장님이랑 제일 친한 친구같아. 저녁에 일 같이 하는 거 같은데... 노래도 하고, 집은 여기서 안 멀어.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "오 관심이 없어서 잘은 모르는데 낮엔 오디션도 보고 그러는지 기획사 있는데 다니고, 저녁에 여기서 노래 부르더라구... 혹시 이암이 잘 알아?"
        },
        {
            "cue": "사실 내 꿈이 싱어송라이터거든!",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "응? 작사 작곡하고 노래까지 부르는 사람."
        },
        {
            "cue": "아, 만능 엔터테이너?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "만능 엔터테이너?"
        },
        {
            "cue": "어, 김삿갓삿갓 김김삿갓삿갓...",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "어, 김삿갓삿갓 김김삿갓삿갓... (심취했다가 민망해서) 그런데 그게 왜?"
        },
        {
            "cue": "음... 있긴 하지?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "누구?"
        }
    ],
    "5. 썸데이 바 재방문 및 이암과의 교감": [
        {
            "cue": "초대해 주셔서 감사해요.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "와! 진짜로 또 오실 줄이야."
        },
        {
            "cue": "네, 아 저 안 마셔도 되는데...",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "어? 안 되는데... 제가 이거 만들어 드리려고 생 사과도 사 왔는데요, 드셔야죠."
        },
        {
            "cue": "네 고맙습니다.",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "연수씨도 한 잔 드릴까요?"
        },
        {
            "cue": "그게 대체 무슨 말이에요?",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "저 친구랑 저랑 같이 만든 곡이 있는데, 가사를 저 친구가 썼거든요."
        },
        {
            "cue": "제목은 썸데이야. 어때?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "아..."
        },
        {
            "cue": "별로야?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "와! 어떻게 이런 글이 나오지? 난 도대체 무슨 노래를 부른 거야..."
        },
        {
            "cue": "일단은 간단하게 먼저 써 본 거야. 좋으면 계속 써볼까?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "어, 너무 좋아. 너무너무 좋아!"
        },
        {
            "cue": "어머, 어떻게 해.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "이로울 이에 어두울 암. 아버지가 동사무소에서 한자를 잘못 고르셨대."
        },
        {
            "cue": "와 그렇게는 생각 안 해봤는데... 글을 써서 그런가 어떻게 그런 생각을 하지?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "빛의 입장에서는 어둠이 엄청 고맙지 않나? 빛을 더 밝게, 더 필요하게 만들어 주잖아."
        },
        {
            "cue": "어?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "네가 빛이었으면 좋겠다."
        },
        {
            "cue": "할게, 내가... 빛.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "아니야..."
        },
        {
            "cue": "어? 아닌가?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "어?"
        },
        {
            "cue": "나도 처음이라... 아, 그럼 뽀뽀부터 하는 건가부다...",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "아닌가?"
        },
        {
            "cue": "아닌가?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "맞는 것 같아. 아니, 하고 싶어. 갈게."
        }
    ],
    "6. 바다 여행과 보드카 가사 작업": [
        {
            "cue": "뭐가?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "저렇게 해변이 밀어내고 내치고 하는데 지치지 않아."
        },
        {
            "cue": "해줘~!",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "뭐? 부끄럽게 이걸 어떻게 불러"
        },
        {
            "cue": "하고 싶어? 그럼 마셔! 네 뜨겁지만 투명한 피부를 온전히 느끼고 싶어.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "네가 내게 채워지는 순간을 기다리고 있어."
        }
    ],
    "7. 임신 고백과 갈등 장면": [
        {
            "cue": "축하해 줘~!",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "축하해."
        },
        {
            "cue": "그리고 이건 이암이한테도 말 안 한 건데... 나 임신했어!",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "이암, 연수, 연희 어?!?! (스르르 쓰러짐)"
        },
        {
            "cue": "초대해 주셔서 감사해요.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "와! 진짜로 또 오실 줄이야."
        },
        {
            "cue": "아니, 말도 마. 특별히 뭐 하는 것도 없는데 한 번 가면 10만원이 넘게 깨져. 2주에 한 번씩 오라는데 그걸 어떻게 가니, 그래서 한 달에 한 번씩 가다가 이번 달엔 아직 안 갔지 뭐. 다음 달에 가면, 돈 20만원 아끼는 거야.",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "그래도 되나...? 그래도 가야 하지 않아?"
        },
        {
            "cue": "오~ 의리!!",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "진심이야 지해야."
        },
        {
            "cue": "어허! 거기까지! 나 간다. 쟤네 정분 나겠어...",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "그래... 가~ 몸 조심하고."
        },
        {
            "cue": "그냥... 보고 싶어서.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "... 말도 없이... 아, 오늘은 어땠어?"
        },
        {
            "cue": "돈 때문에 그래?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "뭐 물론 돈이 중요하다고도 말 못하고... 그런데, 있잖아 나 진짜 괜찮아."
        },
        {
            "cue": "낮에 일 하잖아.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그건... 이거랑 다른 거지."
        },
        {
            "cue": "돈 버는 일은 낮에 하는 거 아니었어?",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "언제까지 그 일을 할 수는 없잖아. 나도 결국 음악을 해야 하니까."
        },
        {
            "cue": "아니, 그래. 그럼 둘 중에 하나는 그만하고 나랑 시간을 보낼 순 없나 물어보려고 했어.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "왜?"
        },
        {
            "cue": "그냥.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "지금 되게 중요한 시기야."
        },
        {
            "cue": "나도 그래.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "갑자기 왜 그래."
        },
        {
            "cue": "갑자기가 아니야. 계속 얘기하고 싶었어. 같이 내가 쓴 가사 읽으면서 그렇게 서로 이야기도 하고 너 노래도 만들고... 우리 그런 시간 못 가진지 꽤 오래 됐잖아.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "아니, 가사들 어디 가는 거 아니잖아. 시간 나면 보고 그렇게 같이 만들고 하면 되지."
        },
        {
            "cue": "언제까지 그럴 건데...",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그거야... 잘 모르지..."
        },
        {
            "cue": "아니잖아 네 진심은 네가 말했던 그 꿈이잖아 사람들이 뭘 원하든 네가 하고 싶은 말을 해 줘 돈보다 중요한 건 네가 전하고 싶은 그 말 진짜 네 이야길 네 목소리로 불러야 해",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "진심이 뭐야 그게 무슨 소용 아무도 듣지 않으면 다 무슨 의미야"
        },
        {
            "cue": "네가 하고 싶은 말은 뭘까",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "내가 하고 싶은 말은 뭔데"
        },
        {
            "cue": "할 말만 있으면 돼. 네가 할 말이 있으면 들으러 오는 사람이 생겨",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "어떻게 하길 원해."
        },
        {
            "cue": "시간을 내 줘. 나랑 같이 해 줘.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "언제... 그럼 노가다를 뺄까? 돈 벌지 마? 아니면 노래를 하지 마?"
        },
        {
            "cue": "그런 말이 아니잖아.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "왜 그러는 거야 갑자기..."
        },
        {
            "cue": "병원에 갔었어.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "어?"
        },
        {
            "cue": "아, 아기는 건강하다... 그리고 딸이래.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "정말? 딸이라고? 너무 좋아! 지해야... 나 너무 떨려!!!"
        },
        {
            "cue": "그런데... 아니야 나 먼저 갈게.",
            "speaker": "지해",
            "next_speaker": "연희",
            "next_line": "지해야. 잠깐만!"
        }
    ],
    "8. 투병과 마지막 바람": [
        {
            "cue": "미안해,",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "여보세요? 암 병동 연결 좀 부탁드립니다."
        },
        {
            "cue": "네가 여자 잘못 만난 것 같아.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "아니요. 진료 예약 좀 하려고 하는데요..."
        },
        {
            "cue": "알았는데... 언젠간 이렇게 될 거 알았는데, 내가 너무 이기적이었어.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그냥 저 그런 건 모르겠고 진료 예약 좀 잡아 주세요."
        },
        {
            "cue": "나... 네가 너무 좋아서, 잠깐 외면했어. 나 진짜 알고 있었거든? 그런데 외면했어.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그런 소리 제발 그만하고! 지금, 내일이라도... 좀 빠르게 잡아 주세요! 제발 우리 지해 살려 주세요."
        },
        {
            "cue": "미안해. 진짜 미안해.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "지해야. 왜 나와 있어? 약은 먹었어?"
        },
        {
            "cue": "잠깐만... 이리 와 봐.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "응?"
        },
        {
            "cue": "너 뭐하고 왔어.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그냥, 여기저기..."
        },
        {
            "cue": "이제 병원 그만 찾자... 의사 선생님도 홈 호스피스 하라고 하셨잖아.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "아니, 나는 못해. 그렇게 못해."
        },
        {
            "cue": "다른 거 이제 그만 생각하고 내 옆에 있어주면 안 될까? 우리 아기 육아 방법도 너가 알아야 하고.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "아니, 지금 그게 중요한 일이 아니잖아."
        },
        {
            "cue": "이암아... 그게 제일 중요해.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그래 그래... 알아... 너 마음 아는데, 난 못해. 너 포기 못해."
        },
        {
            "cue": "그러지 마. 우리 받아들이고 미래를 준비하자.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "나한테는 이게 미래야. 너 치료 방법 찾고 입원할 병원도 찾고... 내 미래는 너야."
        },
        {
            "cue": "우리 미래는 여기 있잖아.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "너 자꾸 이러면 나 우리 아기 걱정돼서 어떻게 가..."
        },
        {
            "cue": "내 사랑들 다 모였네.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "어."
        },
        {
            "cue": "연수야, 이리 와 봐.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "어."
        },
        {
            "cue": "그만하고 이리 오라니까.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "이것만 좀 더 하고."
        },
        {
            "cue": "연수야. 얼굴 좀 더 보고 싶어. 그만하고 앉아.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "계속 볼 거야. 내일도 보고 일 년 뒤에도 보고!"
        },
        {
            "cue": "그래... 나 있잖아,",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "뭐가?"
        },
        {
            "cue": "하... 조금만 더 살고 싶다. 한 1-2년이면 어떨까, 그래 딱 2년만...",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "그런 소리 하지 마."
        },
        {
            "cue": "그래 그래, 하... 궁금하다.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "뭐가?"
        },
        {
            "cue": "우리 딸. 어떤 아이일까?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "어떤 아이였으면 좋겠는데?"
        },
        {
            "cue": "어떤 아이였으면 좋겠다... 그런 건 없고 그냥 궁금해.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "어떨 것 같은데?"
        },
        {
            "cue": "일단 귀여운 반곱슬에 피부는 좀 까무잡잡할 것 같고? 그래 이거 하나, 키는 컸으면 좋겠다. 그리고 무엇보다 자기주장이 강할 거야.",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "너무 그렇게 기대는 하지 않았으면 좋겠어."
        },
        {
            "cue": "무슨 말이야?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "아니, 그냥... 나중에 실망할 수도 있잖아. 딸이 원하는대로 못 크면... 딸도 그렇게 기대에 못 미치니까... 엄마한테 미안할 수도 있을 거 같고, 그렇지 않을까?"
        },
        {
            "cue": "그러면 어때. 그것도 자기 인생이고... 나는 어떤 선택을 하건 응원하는 사람일텐데?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "정말? 어떤 선택을 해도 응원할 거야?"
        },
        {
            "cue": "아마도?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "아마도가 뭐야."
        },
        {
            "cue": "응?",
            "speaker": "지해",
            "next_speaker": "연수",
            "next_line": "그렇잖아. 제일 필요할 때 없을 거잖아. 학교 처음 입학할 때도 없을 거고, 사춘기 때도 없을 거고 처음 생리했을 때도 없을 거잖아."
        },
        {
            "cue": "부탁이 있어.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "..."
        },
        {
            "cue": "일단 하나. 약속해 줘. 잘 지내겠다고... 내가 너희들한테 받은 도움이 너무 많은데 다 못 돌려줬잖아. 나한테 줬던 도움만큼 너희들도 행복했으면 좋겠어. 그러니까 누가 방해해도, 누가 말려도 절대로 포기하지 마.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그럴게... 알았어 약속할게 잘 지낼게..."
        },
        {
            "cue": "그리고 이거. '나의 노래'야. 이 노래로 오디션 보고 오면 좋겠어. 이게 바로 '지해의 노래'라구! 그러니까 이담에 우리 딸이랑도 같이 불렀으면 좋겠어. 약속.",
            "speaker": "지해",
            "next_speaker": "이암",
            "next_line": "그래... 약속..."
        }
    ]
}

# 세션 상태 초기화 (페이지를 이동해도 연습 위치 유지)
if "selected_scene" not in st.session_state:
    st.session_state.selected_scene = list(SCENES.keys())[0]
if "line_index" not in st.session_state:
    st.session_state.line_index = 0

st.title("🎭 뮤지컬 <썸데이> 지해 연습장")

# 1. 상단: 연습하고 싶은 장면(신) 선택 셀렉트박스
scene_list = list(SCENES.keys())
selected_scene = st.selectbox(
    "📂 연습할 장면을 선택하세요", 
    scene_list, 
    index=scene_list.index(st.session_state.selected_scene)
)

# 장면이 바뀌면 대사 번호를 처음으로 리셋
if selected_scene != st.session_state.selected_scene:
    st.session_state.selected_scene = selected_scene
    st.session_state.line_index = 0
    st.rerun()

current_script = SCENES[st.session_state.selected_scene]
max_idx = len(current_script) - 1

# 현재 진행 상황 표시
st.progress((st.session_state.line_index + 1) / len(current_script))
st.caption(f"진행 상황: {st.session_state.line_index + 1} / {len(current_script)} 대사")

st.markdown("---")

# 2. 현재 지해의 대사 큐(Cue) 보여주기
current_data = current_script[st.session_state.line_index]
st.markdown("### 🗣️ **지해 대사 (내 대사)**")
st.info(f"\"{current_data['cue']}\"")

st.markdown("---")

# 3. 이전 / 다음 이동 버튼
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ 이전 대사", use_container_width=True):
        if st.session_state.line_index > 0:
            st.session_state.line_index -= 1
            st.rerun()

with col2:
    if st.button("➡️ 다음 대사", use_container_width=True):
        if st.session_state.line_index < max_idx:
            st.session_state.line_index += 1
            st.rerun()

# 4. 상대방 대사 확인 영역
show_next = st.checkbox("💡 상대방 대사 보기 (정답 확인)", value=True)

if show_next:
    st.success(f"**[{current_data['next_speaker']}]**\n\n💬 {current_data['next_line']}")

# 처음부터 다시 버튼
if st.button("🔄 이 장면 처음부터 다시", use_container_width=True):
    st.session_state.line_index = 0
    st.rerun()
