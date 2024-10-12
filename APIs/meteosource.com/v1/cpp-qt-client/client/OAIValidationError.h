/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIValidationError.h
 *
 * 
 */

#ifndef OAIValidationError_H
#define OAIValidationError_H

#include <QJsonObject>

#include "OAILocation_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIValidationError : public OAIObject {
public:
    OAIValidationError();
    OAIValidationError(QString json);
    ~OAIValidationError() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAILocation_inner> getLoc() const;
    void setLoc(const QList<OAILocation_inner> &loc);
    bool is_loc_Set() const;
    bool is_loc_Valid() const;

    QString getMsg() const;
    void setMsg(const QString &msg);
    bool is_msg_Set() const;
    bool is_msg_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAILocation_inner> m_loc;
    bool m_loc_isSet;
    bool m_loc_isValid;

    QString m_msg;
    bool m_msg_isSet;
    bool m_msg_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIValidationError)

#endif // OAIValidationError_H
