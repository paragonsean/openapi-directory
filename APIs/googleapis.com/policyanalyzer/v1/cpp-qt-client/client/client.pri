QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleCloudPolicyanalyzerV1Activity.h \
    $${PWD}/OAIGoogleCloudPolicyanalyzerV1ObservationPeriod.h \
    $${PWD}/OAIGoogleCloudPolicyanalyzerV1QueryActivityResponse.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIGoogleCloudPolicyanalyzerV1Activity.cpp \
    $${PWD}/OAIGoogleCloudPolicyanalyzerV1ObservationPeriod.cpp \
    $${PWD}/OAIGoogleCloudPolicyanalyzerV1QueryActivityResponse.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
