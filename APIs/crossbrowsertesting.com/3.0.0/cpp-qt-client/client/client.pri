QT += network

HEADERS += \
# Models
    $${PWD}/OAIComparison.h \
    $${PWD}/OAIElement.h \
    $${PWD}/OAIFull_comparison_test.h \
    $${PWD}/OAIFull_comparison_test_base.h \
    $${PWD}/OAIScreenshot.h \
    $${PWD}/OAISingle_comparison_test.h \
    $${PWD}/OAITarget.h \
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
    $${PWD}/OAIComparison.cpp \
    $${PWD}/OAIElement.cpp \
    $${PWD}/OAIFull_comparison_test.cpp \
    $${PWD}/OAIFull_comparison_test_base.cpp \
    $${PWD}/OAIScreenshot.cpp \
    $${PWD}/OAISingle_comparison_test.cpp \
    $${PWD}/OAITarget.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
