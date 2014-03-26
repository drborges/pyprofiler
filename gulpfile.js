var gulp = require('gulp'),
    plumber = require('gulp-plumber'),
    watch = require('gulp-watch'),
    shell = require('gulp-shell');

var nosetests = shell('nosetests tests');

gulp.task('default', function () {
  gulp.run('watch');
});

gulp.task('spec', function () {
  gulp.src('./')
      .pipe(nosetests);
})

gulp.task('watch', function () {
  watch({ glob: './{lib,tests}/*.py' })
    .pipe(plumber())
    .pipe(nosetests);
});