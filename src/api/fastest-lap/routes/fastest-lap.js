'use strict';

/**
 * fastest-lap router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::fastest-lap.fastest-lap');
