QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountbalance_9.h \
    $${PWD}/OAICardacceptor_2.h \
    $${PWD}/OAIRepower_5.h \
    $${PWD}/OAIRepower_5_wrapper.h \
    $${PWD}/OAIRepowerrequest_1.h \
    $${PWD}/OAIRepowerrequest_1_wrapper.h \
    $${PWD}/OAIRepowerreversal_11.h \
    $${PWD}/OAIRepowerreversal_11_wrapper.h \
    $${PWD}/OAIRepowerreversalrequest_10.h \
    $${PWD}/OAIRepowerreversalrequest_10_wrapper.h \
    $${PWD}/OAIResponse_14.h \
    $${PWD}/OAIResponse_8.h \
    $${PWD}/OAITransaction_13.h \
    $${PWD}/OAITransaction_7.h \
    $${PWD}/OAITransactionamount_3.h \
    $${PWD}/OAITransactionfee_4.h \
    $${PWD}/OAITransactionhistory_12.h \
    $${PWD}/OAITransactionhistory_6.h \
# APIs
    $${PWD}/OAIRePowerTransferApi.h \
    $${PWD}/OAIRePowerTransferReversalApi.h \
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
    $${PWD}/OAIAccountbalance_9.cpp \
    $${PWD}/OAICardacceptor_2.cpp \
    $${PWD}/OAIRepower_5.cpp \
    $${PWD}/OAIRepower_5_wrapper.cpp \
    $${PWD}/OAIRepowerrequest_1.cpp \
    $${PWD}/OAIRepowerrequest_1_wrapper.cpp \
    $${PWD}/OAIRepowerreversal_11.cpp \
    $${PWD}/OAIRepowerreversal_11_wrapper.cpp \
    $${PWD}/OAIRepowerreversalrequest_10.cpp \
    $${PWD}/OAIRepowerreversalrequest_10_wrapper.cpp \
    $${PWD}/OAIResponse_14.cpp \
    $${PWD}/OAIResponse_8.cpp \
    $${PWD}/OAITransaction_13.cpp \
    $${PWD}/OAITransaction_7.cpp \
    $${PWD}/OAITransactionamount_3.cpp \
    $${PWD}/OAITransactionfee_4.cpp \
    $${PWD}/OAITransactionhistory_12.cpp \
    $${PWD}/OAITransactionhistory_6.cpp \
# APIs
    $${PWD}/OAIRePowerTransferApi.cpp \
    $${PWD}/OAIRePowerTransferReversalApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
