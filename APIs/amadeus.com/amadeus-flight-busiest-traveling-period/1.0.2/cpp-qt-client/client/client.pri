QT += network

HEADERS += \
# Models
    $${PWD}/OAIAir_Traffic.h \
    $${PWD}/OAIAnalytics.h \
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAISuccess.h \
    $${PWD}/OAITravelers.h \
# APIs
    $${PWD}/OAIAirTrafficApi.h \
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
    $${PWD}/OAIAir_Traffic.cpp \
    $${PWD}/OAIAnalytics.cpp \
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAISuccess.cpp \
    $${PWD}/OAITravelers.cpp \
# APIs
    $${PWD}/OAIAirTrafficApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
