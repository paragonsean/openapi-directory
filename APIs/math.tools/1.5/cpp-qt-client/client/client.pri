QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIBaseConversionApi.h \
    $${PWD}/OAINumberChecksApi.h \
    $${PWD}/OAINumberFactsApi.h \
    $${PWD}/OAINumberGenerationApi.h \
    $${PWD}/OAINumberOfTheDayApi.h \
    $${PWD}/OAINumberSystemsConversionApi.h \
    $${PWD}/OAIPIApi.h \
    $${PWD}/OAIPrimeApi.h \
    $${PWD}/OAISpellApi.h \
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
    $${PWD}/OAIBaseConversionApi.cpp \
    $${PWD}/OAINumberChecksApi.cpp \
    $${PWD}/OAINumberFactsApi.cpp \
    $${PWD}/OAINumberGenerationApi.cpp \
    $${PWD}/OAINumberOfTheDayApi.cpp \
    $${PWD}/OAINumberSystemsConversionApi.cpp \
    $${PWD}/OAIPIApi.cpp \
    $${PWD}/OAIPrimeApi.cpp \
    $${PWD}/OAISpellApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
