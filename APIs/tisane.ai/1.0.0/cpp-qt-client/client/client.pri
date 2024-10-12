QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetFamilyDetails_200_response.h \
    $${PWD}/OAIListHypernyms_200_response_inner_inner.h \
    $${PWD}/OAIListInflectedForms_200_response_inner.h \
    $${PWD}/OAIListInflectedForms_200_response_inner_features_inner.h \
    $${PWD}/OAIListWordSenses_200_response_inner.h \
    $${PWD}/OAIListWordSenses_200_response_inner_families_inner.h \
    $${PWD}/OAIListWordSenses_200_response_inner_features_inner.h \
# APIs
    $${PWD}/OAILanguageModelDirectAccessApi.h \
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
    $${PWD}/OAIGetFamilyDetails_200_response.cpp \
    $${PWD}/OAIListHypernyms_200_response_inner_inner.cpp \
    $${PWD}/OAIListInflectedForms_200_response_inner.cpp \
    $${PWD}/OAIListInflectedForms_200_response_inner_features_inner.cpp \
    $${PWD}/OAIListWordSenses_200_response_inner.cpp \
    $${PWD}/OAIListWordSenses_200_response_inner_families_inner.cpp \
    $${PWD}/OAIListWordSenses_200_response_inner_features_inner.cpp \
# APIs
    $${PWD}/OAILanguageModelDirectAccessApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
