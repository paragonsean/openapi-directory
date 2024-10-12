QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIBrailleApi.h \
    $${PWD}/OAICharactersApi.h \
    $${PWD}/OAIDialectApi.h \
    $${PWD}/OAIElvishApi.h \
    $${PWD}/OAIEnglishApi.h \
    $${PWD}/OAIGameOfThronesApi.h \
    $${PWD}/OAIInternetFADApi.h \
    $${PWD}/OAIMorseApi.h \
    $${PWD}/OAIPigLatinApi.h \
    $${PWD}/OAIStartrekApi.h \
    $${PWD}/OAIStarwarsApi.h \
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
    $${PWD}/OAIBrailleApi.cpp \
    $${PWD}/OAICharactersApi.cpp \
    $${PWD}/OAIDialectApi.cpp \
    $${PWD}/OAIElvishApi.cpp \
    $${PWD}/OAIEnglishApi.cpp \
    $${PWD}/OAIGameOfThronesApi.cpp \
    $${PWD}/OAIInternetFADApi.cpp \
    $${PWD}/OAIMorseApi.cpp \
    $${PWD}/OAIPigLatinApi.cpp \
    $${PWD}/OAIStartrekApi.cpp \
    $${PWD}/OAIStarwarsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
