QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorBodyContract.h \
    $${PWD}/OAIErrorFieldContract.h \
    $${PWD}/OAIPolicySnippetContract.h \
    $${PWD}/OAIPolicySnippetsCollection.h \
    $${PWD}/OAIRegionContract.h \
    $${PWD}/OAIRegionListResult.h \
# APIs
    $${PWD}/OAIPolicySnippetsApi.h \
    $${PWD}/OAIRegionsApi.h \
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
    $${PWD}/OAIErrorBodyContract.cpp \
    $${PWD}/OAIErrorFieldContract.cpp \
    $${PWD}/OAIPolicySnippetContract.cpp \
    $${PWD}/OAIPolicySnippetsCollection.cpp \
    $${PWD}/OAIRegionContract.cpp \
    $${PWD}/OAIRegionListResult.cpp \
# APIs
    $${PWD}/OAIPolicySnippetsApi.cpp \
    $${PWD}/OAIRegionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
