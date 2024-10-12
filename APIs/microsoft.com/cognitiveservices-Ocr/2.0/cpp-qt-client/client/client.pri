QT += network

HEADERS += \
# Models
    $${PWD}/OAIComputerVisionError.h \
    $${PWD}/OAIImageUrl.h \
    $${PWD}/OAILine.h \
    $${PWD}/OAIOperationStatus.h \
    $${PWD}/OAIReadOperationResult.h \
    $${PWD}/OAITextOperationResult.h \
    $${PWD}/OAITextRecognitionResult.h \
    $${PWD}/OAIWord.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIComputerVisionError.cpp \
    $${PWD}/OAIImageUrl.cpp \
    $${PWD}/OAILine.cpp \
    $${PWD}/OAIOperationStatus.cpp \
    $${PWD}/OAIReadOperationResult.cpp \
    $${PWD}/OAITextOperationResult.cpp \
    $${PWD}/OAITextRecognitionResult.cpp \
    $${PWD}/OAIWord.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
