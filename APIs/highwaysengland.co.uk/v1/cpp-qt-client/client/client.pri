QT += network

HEADERS += \
# Models
    $${PWD}/OAIArea.h \
    $${PWD}/OAIAreaResponse.h \
    $${PWD}/OAIDailyQualityResponse.h \
    $${PWD}/OAIOverallQualityResponse.h \
    $${PWD}/OAIQualities.h \
    $${PWD}/OAISiteResponse.h \
    $${PWD}/OAISiteResult.h \
    $${PWD}/OAISiteType.h \
    $${PWD}/OAISiteTypeLayer.h \
    $${PWD}/OAISiteTypeResponse.h \
    $${PWD}/OAISites.h \
# APIs
    $${PWD}/OAIAreasApi.h \
    $${PWD}/OAIQualityApi.h \
    $${PWD}/OAIReportsApi.h \
    $${PWD}/OAISiteTypesApi.h \
    $${PWD}/OAISitesApi.h \
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
    $${PWD}/OAIArea.cpp \
    $${PWD}/OAIAreaResponse.cpp \
    $${PWD}/OAIDailyQualityResponse.cpp \
    $${PWD}/OAIOverallQualityResponse.cpp \
    $${PWD}/OAIQualities.cpp \
    $${PWD}/OAISiteResponse.cpp \
    $${PWD}/OAISiteResult.cpp \
    $${PWD}/OAISiteType.cpp \
    $${PWD}/OAISiteTypeLayer.cpp \
    $${PWD}/OAISiteTypeResponse.cpp \
    $${PWD}/OAISites.cpp \
# APIs
    $${PWD}/OAIAreasApi.cpp \
    $${PWD}/OAIQualityApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
    $${PWD}/OAISiteTypesApi.cpp \
    $${PWD}/OAISitesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
