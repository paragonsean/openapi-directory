QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorFieldContract.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIPolicyCollection.h \
    $${PWD}/OAIPolicyContract.h \
    $${PWD}/OAIPolicyContractProperties.h \
    $${PWD}/OAIPolicySnippetContract.h \
    $${PWD}/OAIPolicySnippetsCollection.h \
    $${PWD}/OAIRegionContract.h \
    $${PWD}/OAIRegionListResult.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIPolicyApi.h \
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
    $${PWD}/OAIErrorFieldContract.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIPolicyCollection.cpp \
    $${PWD}/OAIPolicyContract.cpp \
    $${PWD}/OAIPolicyContractProperties.cpp \
    $${PWD}/OAIPolicySnippetContract.cpp \
    $${PWD}/OAIPolicySnippetsCollection.cpp \
    $${PWD}/OAIRegionContract.cpp \
    $${PWD}/OAIRegionListResult.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIPolicyApi.cpp \
    $${PWD}/OAIPolicySnippetsApi.cpp \
    $${PWD}/OAIRegionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
