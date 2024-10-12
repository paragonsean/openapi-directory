QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIDocumentClassificationApi.h \
    $${PWD}/OAIInformationRetrievalApi.h \
    $${PWD}/OAIMetricsApi.h \
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
# APIs
    $${PWD}/OAIDocumentClassificationApi.cpp \
    $${PWD}/OAIInformationRetrievalApi.cpp \
    $${PWD}/OAIMetricsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
