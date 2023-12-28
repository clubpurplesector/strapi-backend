'use strict';

/**
 * pit-stop service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::pit-stop.pit-stop');
