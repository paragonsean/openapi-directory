/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPropertyRoomModelResults.h
 *
 * Holds results from a paged query returning PropertyRoomModel values
 */

#ifndef OAIPropertyRoomModelResults_H
#define OAIPropertyRoomModelResults_H

#include <QJsonObject>

#include "OAIPropertyRoomModel.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPropertyRoomModel;

class OAIPropertyRoomModelResults : public OAIObject {
public:
    OAIPropertyRoomModelResults();
    OAIPropertyRoomModelResults(QString json);
    ~OAIPropertyRoomModelResults() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCount() const;
    void setCount(const qint32 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    QList<OAIPropertyRoomModel> getData() const;
    void setData(const QList<OAIPropertyRoomModel> &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    QList<OAIPropertyRoomModel> m_data;
    bool m_data_isSet;
    bool m_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPropertyRoomModelResults)

#endif // OAIPropertyRoomModelResults_H
