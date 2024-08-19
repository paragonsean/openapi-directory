QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiConfig.h \
    $${PWD}/OAICategory.h \
    $${PWD}/OAIDocument.h \
    $${PWD}/OAIDocumentResult.h \
    $${PWD}/OAIPartOfSpeech.h \
    $${PWD}/OAISentence.h \
    $${PWD}/OAISentencePart.h \
    $${PWD}/OAISlangWord.h \
    $${PWD}/OAIStorageInfo.h \
# APIs
    $${PWD}/OAIAnalyzeApi.h \
    $${PWD}/OAICategorizeApi.h \
    $${PWD}/OAIExtractApi.h \
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
    $${PWD}/OAIApiConfig.cpp \
    $${PWD}/OAICategory.cpp \
    $${PWD}/OAIDocument.cpp \
    $${PWD}/OAIDocumentResult.cpp \
    $${PWD}/OAIPartOfSpeech.cpp \
    $${PWD}/OAISentence.cpp \
    $${PWD}/OAISentencePart.cpp \
    $${PWD}/OAISlangWord.cpp \
    $${PWD}/OAIStorageInfo.cpp \
# APIs
    $${PWD}/OAIAnalyzeApi.cpp \
    $${PWD}/OAICategorizeApi.cpp \
    $${PWD}/OAIExtractApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
