QT += network

HEADERS += \
# Models
    $${PWD}/OAIMapsAccount.h \
    $${PWD}/OAIMapsAccountCreateParameters.h \
    $${PWD}/OAIMapsAccountKeys.h \
    $${PWD}/OAIMapsAccountProperties.h \
    $${PWD}/OAIMapsAccountUpdateParameters.h \
    $${PWD}/OAIMapsAccounts.h \
    $${PWD}/OAIMapsKeySpecification.h \
    $${PWD}/OAIMapsOperations.h \
    $${PWD}/OAIMapsOperations_value_inner.h \
    $${PWD}/OAIMapsOperations_value_inner_display.h \
    $${PWD}/OAIMaps_ListOperations_default_response.h \
    $${PWD}/OAIMaps_ListOperations_default_response_additionalInfo_inner.h \
    $${PWD}/OAIPrivateAtlas.h \
    $${PWD}/OAIPrivateAtlasCreateParameters.h \
    $${PWD}/OAIPrivateAtlasList.h \
    $${PWD}/OAIPrivateAtlasProperties.h \
    $${PWD}/OAIPrivateAtlasUpdateParameters.h \
    $${PWD}/OAISku.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIPrivateAtlasesApi.h \
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
    $${PWD}/OAIMapsAccount.cpp \
    $${PWD}/OAIMapsAccountCreateParameters.cpp \
    $${PWD}/OAIMapsAccountKeys.cpp \
    $${PWD}/OAIMapsAccountProperties.cpp \
    $${PWD}/OAIMapsAccountUpdateParameters.cpp \
    $${PWD}/OAIMapsAccounts.cpp \
    $${PWD}/OAIMapsKeySpecification.cpp \
    $${PWD}/OAIMapsOperations.cpp \
    $${PWD}/OAIMapsOperations_value_inner.cpp \
    $${PWD}/OAIMapsOperations_value_inner_display.cpp \
    $${PWD}/OAIMaps_ListOperations_default_response.cpp \
    $${PWD}/OAIMaps_ListOperations_default_response_additionalInfo_inner.cpp \
    $${PWD}/OAIPrivateAtlas.cpp \
    $${PWD}/OAIPrivateAtlasCreateParameters.cpp \
    $${PWD}/OAIPrivateAtlasList.cpp \
    $${PWD}/OAIPrivateAtlasProperties.cpp \
    $${PWD}/OAIPrivateAtlasUpdateParameters.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIPrivateAtlasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
