QT += network

HEADERS += \
# Models
    $${PWD}/OAIEntitiesResponse.h \
    $${PWD}/OAIEntity.h \
    $${PWD}/OAIEntrystringlong.h \
    $${PWD}/OAIInformation_about_a_user_account_.h \
    $${PWD}/OAILabel.h \
    $${PWD}/OAILemmatizeResponse.h \
    $${PWD}/OAIRequest.h \
    $${PWD}/OAIResponse_for_the_text_correction.h \
    $${PWD}/OAISentimentResponse.h \
    $${PWD}/OAITopicResponse.h \
# APIs
    $${PWD}/OAIAccountApi.h \
    $${PWD}/OAIGeneeaApiS1Api.h \
    $${PWD}/OAIStatusApiApi.h \
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
    $${PWD}/OAIEntitiesResponse.cpp \
    $${PWD}/OAIEntity.cpp \
    $${PWD}/OAIEntrystringlong.cpp \
    $${PWD}/OAIInformation_about_a_user_account_.cpp \
    $${PWD}/OAILabel.cpp \
    $${PWD}/OAILemmatizeResponse.cpp \
    $${PWD}/OAIRequest.cpp \
    $${PWD}/OAIResponse_for_the_text_correction.cpp \
    $${PWD}/OAISentimentResponse.cpp \
    $${PWD}/OAITopicResponse.cpp \
# APIs
    $${PWD}/OAIAccountApi.cpp \
    $${PWD}/OAIGeneeaApiS1Api.cpp \
    $${PWD}/OAIStatusApiApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
