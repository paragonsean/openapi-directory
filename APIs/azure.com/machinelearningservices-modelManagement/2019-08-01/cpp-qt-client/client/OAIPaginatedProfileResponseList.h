/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPaginatedProfileResponseList.h
 *
 * A paginated list of ProfileResponses.
 */

#ifndef OAIPaginatedProfileResponseList_H
#define OAIPaginatedProfileResponseList_H

#include <QJsonObject>

#include "OAIProfileResponse.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIProfileResponse;

class OAIPaginatedProfileResponseList : public OAIObject {
public:
    OAIPaginatedProfileResponseList();
    OAIPaginatedProfileResponseList(QString json);
    ~OAIPaginatedProfileResponseList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    QList<OAIProfileResponse> getValue() const;
    void setValue(const QList<OAIProfileResponse> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;

    QList<OAIProfileResponse> m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPaginatedProfileResponseList)

#endif // OAIPaginatedProfileResponseList_H
