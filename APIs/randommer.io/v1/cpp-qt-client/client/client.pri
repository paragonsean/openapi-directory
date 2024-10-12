QT += network

HEADERS += \
# Models
    $${PWD}/OAICaseType.h \
    $${PWD}/OAIIdType.h \
    $${PWD}/OAILoremType.h \
    $${PWD}/OAINameType.h \
    $${PWD}/OAINumberValidation.h \
    $${PWD}/OAITextActionType.h \
    $${PWD}/OAITextDto.h \
    $${PWD}/OAITextType.h \
# APIs
    $${PWD}/OAICardApi.h \
    $${PWD}/OAIFinanceApi.h \
    $${PWD}/OAIMiscApi.h \
    $${PWD}/OAINameApi.h \
    $${PWD}/OAIPhoneApi.h \
    $${PWD}/OAISocialNumberApi.h \
    $${PWD}/OAITextApi.h \
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
    $${PWD}/OAICaseType.cpp \
    $${PWD}/OAIIdType.cpp \
    $${PWD}/OAILoremType.cpp \
    $${PWD}/OAINameType.cpp \
    $${PWD}/OAINumberValidation.cpp \
    $${PWD}/OAITextActionType.cpp \
    $${PWD}/OAITextDto.cpp \
    $${PWD}/OAITextType.cpp \
# APIs
    $${PWD}/OAICardApi.cpp \
    $${PWD}/OAIFinanceApi.cpp \
    $${PWD}/OAIMiscApi.cpp \
    $${PWD}/OAINameApi.cpp \
    $${PWD}/OAIPhoneApi.cpp \
    $${PWD}/OAISocialNumberApi.cpp \
    $${PWD}/OAITextApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
