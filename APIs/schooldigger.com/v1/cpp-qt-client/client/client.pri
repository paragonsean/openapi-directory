QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIBoundary.h \
    $${PWD}/OAIAPICounty.h \
    $${PWD}/OAIAPIDistrict.h \
    $${PWD}/OAIAPIDistrict1Summary.h \
    $${PWD}/OAIAPIDistrictList.h \
    $${PWD}/OAIAPIDistrictListRank.h \
    $${PWD}/OAIAPIDistrictSum.h \
    $${PWD}/OAIAPILEARankHistory.h \
    $${PWD}/OAIAPILEAYearlyDetail.h \
    $${PWD}/OAIAPILatLong.h \
    $${PWD}/OAIAPILocation.h \
    $${PWD}/OAIAPIPolyline.h \
    $${PWD}/OAIAPIRankHistory.h \
    $${PWD}/OAIAPISchool10Full.h \
    $${PWD}/OAIAPISchool1Summary.h \
    $${PWD}/OAIAPISchoolList.h \
    $${PWD}/OAIAPISchoolListRank.h \
    $${PWD}/OAIAPITestScore.h \
    $${PWD}/OAIAPITestScoreWrapper.h \
    $${PWD}/OAIAPIYearlyDemographics.h \
# APIs
    $${PWD}/OAIDistrictsApi.h \
    $${PWD}/OAIRankingsApi.h \
    $${PWD}/OAISchoolsApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIAPIBoundary.cpp \
    $${PWD}/OAIAPICounty.cpp \
    $${PWD}/OAIAPIDistrict.cpp \
    $${PWD}/OAIAPIDistrict1Summary.cpp \
    $${PWD}/OAIAPIDistrictList.cpp \
    $${PWD}/OAIAPIDistrictListRank.cpp \
    $${PWD}/OAIAPIDistrictSum.cpp \
    $${PWD}/OAIAPILEARankHistory.cpp \
    $${PWD}/OAIAPILEAYearlyDetail.cpp \
    $${PWD}/OAIAPILatLong.cpp \
    $${PWD}/OAIAPILocation.cpp \
    $${PWD}/OAIAPIPolyline.cpp \
    $${PWD}/OAIAPIRankHistory.cpp \
    $${PWD}/OAIAPISchool10Full.cpp \
    $${PWD}/OAIAPISchool1Summary.cpp \
    $${PWD}/OAIAPISchoolList.cpp \
    $${PWD}/OAIAPISchoolListRank.cpp \
    $${PWD}/OAIAPITestScore.cpp \
    $${PWD}/OAIAPITestScoreWrapper.cpp \
    $${PWD}/OAIAPIYearlyDemographics.cpp \
# APIs
    $${PWD}/OAIDistrictsApi.cpp \
    $${PWD}/OAIRankingsApi.cpp \
    $${PWD}/OAISchoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
