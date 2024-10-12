QT += network

HEADERS += \
# Models
    $${PWD}/OAIAbout.h \
    $${PWD}/OAIAbout_apiVersion.h \
    $${PWD}/OAIEc.h \
    $${PWD}/OAIEc_alphabetSequence_inner.h \
    $${PWD}/OAIEc_entropyDistribution_inner.h \
    $${PWD}/OAIEc_keyboardSequence_inner.h \
    $${PWD}/OAIEc_numberSequence_inner.h \
    $${PWD}/OAIEc_repeatedChars_inner.h \
    $${PWD}/OAIEc_total_inner.h \
    $${PWD}/OAIEc_words_inner.h \
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
    $${PWD}/OAIAbout.cpp \
    $${PWD}/OAIAbout_apiVersion.cpp \
    $${PWD}/OAIEc.cpp \
    $${PWD}/OAIEc_alphabetSequence_inner.cpp \
    $${PWD}/OAIEc_entropyDistribution_inner.cpp \
    $${PWD}/OAIEc_keyboardSequence_inner.cpp \
    $${PWD}/OAIEc_numberSequence_inner.cpp \
    $${PWD}/OAIEc_repeatedChars_inner.cpp \
    $${PWD}/OAIEc_total_inner.cpp \
    $${PWD}/OAIEc_words_inner.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
