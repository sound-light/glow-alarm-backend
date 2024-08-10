# 청각 장애인을 위한 시각 알람, Glow Alarm 💡 
스마트 전구를 이용한 시각 알람 어플리케이션

<p align="center">
  <img src="https://github.com/sound-light/.github/assets/131771046/7973a3fa-49ac-48e2-a145-6c9cfef63a73">
</p>

## Project Overview
In the event of a disaster, evacuation alerts are issued but rely solely on sound, becoming ineffectual for those with deaf and hard of hearing, highlighting a critical social inequality. Neuroplasticity suggests that individuals with hearing loss often have enhanced visual capabilities, making visual alarms a preferred method for alerts, as indicated by research in the *Fire Technology journal's* "Alarm Technologies to Wake Sleeping People Who are Deaf or Hard of Hearing (2022)." This underscores the necessity for a visual warning system.


Addressing this need, we developed Glow Alarm, a system providing visual alerts through lights and flashes, aiding those with hearing impairments in recognizing emergency situations promptly. This system utilizes red lights and flashing effects for alerts, seamlessly integrating with current auditory alert systems to ensure quick responses during emergencies, playing a vital role in life-saving situations.


## Backend Team Members

| 윤병욱 [@speculatingwook](https://github.com/speculatingwook)| 이지민 [@clicelee](https://github.com/clicelee)       |
|---------------------------|-----------------------------|
| Backend/PM                | Backend/Designer            |



## Back-end

| Category  | Stack               |
| --------- | ------------------- |
| Framework | - FastAPI 0.109.0   |
| ORM       | - SQLAlchemy 2.0.25 |
| Infra     | - GCP storage       |
| Database  | - MySql 8.0         |


## ERD Table
<p align="center">
  <img width="985" alt="image" src="https://github.com/sound-light/sound-light-backend/assets/105579811/b090b103-f895-406c-b805-e61856c84690">
</p>


## 브랜치 관리 전략

- Git Flow를 사용하여 브랜치를 관리합니다.

- Release,Develop 브랜치는 Pull Request에 리뷰를 진행한 후 merge를 진행합니다.

- 메인 브렌치인 Develop인 경우 리뷰와 PR 을 필수로 하는 깃 protrction이 설정되어 있습니다.

![branchImage](https://user-images.githubusercontent.com/37647483/226156092-df21a222-76c4-41d0-a9f7-46112ae00ce0.jpg)

- Release : 배포시 사용합니다.
- Develop : 완전히 개발이 끝난 부분에 대해서만 Merge를 진행합니다.
- Feature : 기능 개발을 진행할 때 사용합니다.
- Hot-Fix : 배포를 진행한 후 발생한 버그를 수정해야 할 때 사용합니다.
- Main : v1.0.0 , v1.1.0 과 같이 2번째 자리수의 버전 까지를 저장합니다.
  <br><br>
  <b>브랜치 관리 전략 참고 문헌</b><br>
- [우아한 형제들 기술 블로그](http://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)
- [Bitbucket Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## How to run
- build a container with docker
```
docker build -t glow-alarm-app .
```

- run container in local
```
docker run -p 8080:8080 glow-alarm-app
```