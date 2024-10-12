QT += network

HEADERS += \
# Models
    $${PWD}/OAI201_share.h \
    $${PWD}/OAI403.h \
    $${PWD}/OAI405.h \
    $${PWD}/OAI412.h \
    $${PWD}/OAI449.h \
    $${PWD}/OAIAddUserResponse.h \
    $${PWD}/OAIAllowance.h \
    $${PWD}/OAIAllowance_allowanceTransaction.h \
    $${PWD}/OAIAuthentication.h \
    $${PWD}/OAIChore.h \
    $${PWD}/OAIChorelist.h \
    $${PWD}/OAIInline_response_201.h \
    $${PWD}/OAIInline_response_201_1.h \
    $${PWD}/OAIInline_response_202.h \
    $${PWD}/OAIInvalidateApiKey.h \
    $${PWD}/OAINodata.h \
    $${PWD}/OAISuccess.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAIUserlist.h \
    $${PWD}/OAIWish.h \
    $${PWD}/OAIWishlist.h \
# APIs
    $${PWD}/OAIAuthenticationApi.h \
    $${PWD}/OAIKKidApi.h \
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
    $${PWD}/OAI201_share.cpp \
    $${PWD}/OAI403.cpp \
    $${PWD}/OAI405.cpp \
    $${PWD}/OAI412.cpp \
    $${PWD}/OAI449.cpp \
    $${PWD}/OAIAddUserResponse.cpp \
    $${PWD}/OAIAllowance.cpp \
    $${PWD}/OAIAllowance_allowanceTransaction.cpp \
    $${PWD}/OAIAuthentication.cpp \
    $${PWD}/OAIChore.cpp \
    $${PWD}/OAIChorelist.cpp \
    $${PWD}/OAIInline_response_201.cpp \
    $${PWD}/OAIInline_response_201_1.cpp \
    $${PWD}/OAIInline_response_202.cpp \
    $${PWD}/OAIInvalidateApiKey.cpp \
    $${PWD}/OAINodata.cpp \
    $${PWD}/OAISuccess.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAIUserlist.cpp \
    $${PWD}/OAIWish.cpp \
    $${PWD}/OAIWishlist.cpp \
# APIs
    $${PWD}/OAIAuthenticationApi.cpp \
    $${PWD}/OAIKKidApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
