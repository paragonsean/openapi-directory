QT += network

HEADERS += \
# Models
    $${PWD}/OAICountry.h \
    $${PWD}/OAICreatenewsessionRequest.h \
    $${PWD}/OAIEditsessionRequest.h \
    $${PWD}/OAIModifysessiongettingspecificparametersRequest.h \
    $${PWD}/OAINewValue.h \
    $${PWD}/OAIPostalCode.h \
    $${PWD}/OAIPublic.h \
    $${PWD}/OAIPublic1.h \
# APIs
    $${PWD}/OAISegmentApi.h \
    $${PWD}/OAISessionsApi.h \
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
    $${PWD}/OAICountry.cpp \
    $${PWD}/OAICreatenewsessionRequest.cpp \
    $${PWD}/OAIEditsessionRequest.cpp \
    $${PWD}/OAIModifysessiongettingspecificparametersRequest.cpp \
    $${PWD}/OAINewValue.cpp \
    $${PWD}/OAIPostalCode.cpp \
    $${PWD}/OAIPublic.cpp \
    $${PWD}/OAIPublic1.cpp \
# APIs
    $${PWD}/OAISegmentApi.cpp \
    $${PWD}/OAISessionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
