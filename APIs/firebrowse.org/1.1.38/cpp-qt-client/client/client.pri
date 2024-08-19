QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIAnalysesApi.h \
    $${PWD}/OAIArchivesApi.h \
    $${PWD}/OAIMetadataApi.h \
    $${PWD}/OAISamplesApi.h \
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
    $${PWD}/OAIAnalysesApi.cpp \
    $${PWD}/OAIArchivesApi.cpp \
    $${PWD}/OAIMetadataApi.cpp \
    $${PWD}/OAISamplesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
