QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIAspect.h \
    $${PWD}/OAICharity.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIItemDraft.h \
    $${PWD}/OAIItemDraftResponse.h \
    $${PWD}/OAIPricingSummary.h \
    $${PWD}/OAIProduct.h \
# APIs
    $${PWD}/OAIItemDraftApi.h \
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
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAIAspect.cpp \
    $${PWD}/OAICharity.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIItemDraft.cpp \
    $${PWD}/OAIItemDraftResponse.cpp \
    $${PWD}/OAIPricingSummary.cpp \
    $${PWD}/OAIProduct.cpp \
# APIs
    $${PWD}/OAIItemDraftApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
