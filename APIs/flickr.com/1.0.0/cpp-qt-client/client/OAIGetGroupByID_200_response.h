/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetGroupByID_200_response.h
 *
 * 
 */

#ifndef OAIGetGroupByID_200_response_H
#define OAIGetGroupByID_200_response_H

#include <QJsonObject>

#include "OAIGroup.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGroup;

class OAIGetGroupByID_200_response : public OAIObject {
public:
    OAIGetGroupByID_200_response();
    OAIGetGroupByID_200_response(QString json);
    ~OAIGetGroupByID_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGroup getGroup() const;
    void setGroup(const OAIGroup &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    QString getStat() const;
    void setStat(const QString &stat);
    bool is_stat_Set() const;
    bool is_stat_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGroup m_group;
    bool m_group_isSet;
    bool m_group_isValid;

    QString m_stat;
    bool m_stat_isSet;
    bool m_stat_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetGroupByID_200_response)

#endif // OAIGetGroupByID_200_response_H
