QT += network

HEADERS += \
# Models
    $${PWD}/OAIAliasModel.h \
    $${PWD}/OAIClickModel.h \
    $${PWD}/OAIClickModelPg.h \
    $${PWD}/OAIClicksFilterModel.h \
    $${PWD}/OAICreateAliasModel.h \
    $${PWD}/OAICreateAliasResponseModel.h \
    $${PWD}/OAIDestinationModel.h \
    $${PWD}/OAIGetAliasModel.h \
    $${PWD}/OAIGetAliasesModel.h \
    $${PWD}/OAIGetClicksModel.h \
    $${PWD}/OAIMetaTagModel.h \
    $${PWD}/OAISnippetModel.h \
# APIs
    $${PWD}/OAIAliasApi.h \
    $${PWD}/OAIClickApi.h \
    $${PWD}/OAIStatisticsApi.h \
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
    $${PWD}/OAIAliasModel.cpp \
    $${PWD}/OAIClickModel.cpp \
    $${PWD}/OAIClickModelPg.cpp \
    $${PWD}/OAIClicksFilterModel.cpp \
    $${PWD}/OAICreateAliasModel.cpp \
    $${PWD}/OAICreateAliasResponseModel.cpp \
    $${PWD}/OAIDestinationModel.cpp \
    $${PWD}/OAIGetAliasModel.cpp \
    $${PWD}/OAIGetAliasesModel.cpp \
    $${PWD}/OAIGetClicksModel.cpp \
    $${PWD}/OAIMetaTagModel.cpp \
    $${PWD}/OAISnippetModel.cpp \
# APIs
    $${PWD}/OAIAliasApi.cpp \
    $${PWD}/OAIClickApi.cpp \
    $${PWD}/OAIStatisticsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
